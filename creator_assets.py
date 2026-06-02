import re
import textwrap


FALLBACK_MESSAGE = "Not enough transcript content was available to create this asset."
FILLER_PHRASES = {
    "um",
    "uh",
    "erm",
    "hmm",
}
STOPWORDS = {
    "about",
    "after",
    "again",
    "also",
    "because",
    "before",
    "being",
    "between",
    "could",
    "every",
    "first",
    "from",
    "have",
    "into",
    "just",
    "like",
    "more",
    "most",
    "should",
    "that",
    "their",
    "there",
    "this",
    "through",
    "what",
    "when",
    "where",
    "which",
    "with",
    "would",
    "your",
}


def normalize_spaces(text):
    return re.sub(r"\s+", " ", (text or "").strip())


def split_sentences(text):
    clean = normalize_spaces(text)
    if not clean:
        return []
    parts = re.split(r"(?<=[.!?])\s+", clean)
    return [part.strip() for part in parts if part.strip()]


def transcript_topic(text):
    words = extract_keywords(text, limit=5)
    if words:
        return " ".join(word.title() for word in words[:3])
    sentences = split_sentences(text)
    if sentences:
        fallback = re.sub(r"[^a-zA-Z0-9\s]", "", sentences[0])
        return " ".join(fallback.split()[:5]).title() or "Your Video"
    return "Your Video"


def clean_sentence(sentence):
    words = []
    for word in normalize_spaces(sentence).split():
        bare = re.sub(r"[^a-zA-Z ]", "", word).lower()
        if bare in FILLER_PHRASES:
            continue
        words.append(word)
    cleaned = " ".join(words).strip()
    if cleaned and cleaned[-1] not in ".!?":
        cleaned += "."
    return cleaned


def clean_transcript(text, width=88):
    sentences = [clean_sentence(sentence) for sentence in split_sentences(text)]
    sentences = [sentence for sentence in sentences if sentence]
    if not sentences:
        return FALLBACK_MESSAGE + "\n"

    paragraphs = []
    for index in range(0, len(sentences), 4):
        paragraph = " ".join(sentences[index:index + 4])
        paragraphs.append(textwrap.fill(paragraph, width=width))
    return "\n\n".join(paragraphs) + "\n"


def format_hms(seconds):
    total_seconds = max(0, int(round(float(seconds or 0))))
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    secs = total_seconds % 60
    if hours:
        return f"{hours:02}:{minutes:02}:{secs:02}"
    return f"{minutes:02}:{secs:02}"


def segment_text(segment):
    return normalize_spaces(str(segment.get("text", "")))


def choose_chapter_title(text):
    clean = re.sub(r"[^a-zA-Z0-9\s]", "", normalize_spaces(text))
    words = [word for word in clean.split() if len(word) > 2]
    if not words:
        return "Opening"
    title = " ".join(words[:7])
    return title[:1].upper() + title[1:]


def extract_keywords(text, limit=15):
    counts = {}
    for word in re.findall(r"[a-zA-Z][a-zA-Z0-9-]{2,}", normalize_spaces(text).lower()):
        if word in STOPWORDS:
            continue
        counts[word] = counts.get(word, 0) + 1
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return [word for word, _count in ranked[:limit]]


def generate_chapters(segments, block_seconds=150):
    usable_segments = [
        segment for segment in (segments or [])
        if segment_text(segment) and segment.get("start") is not None
    ]
    if not usable_segments:
        return FALLBACK_MESSAGE + "\n"

    chapters = []
    current_start = float(usable_segments[0].get("start", 0) or 0)
    current_text = []

    for segment in usable_segments:
        start = float(segment.get("start", 0) or 0)
        if current_text and start - current_start >= block_seconds:
            chapters.append((current_start, choose_chapter_title(" ".join(current_text))))
            current_start = start
            current_text = []
        current_text.append(segment_text(segment))

    if current_text:
        chapters.append((current_start, choose_chapter_title(" ".join(current_text))))

    lines = ["Chapters", ""]
    for start, title in chapters:
        lines.append(f"{format_hms(start)} - {title}")
    return "\n".join(lines).strip() + "\n"


def generate_summary(clean_text, max_sentences=3):
    sentences = split_sentences(clean_text)
    if not sentences:
        return FALLBACK_MESSAGE
    selected = sentences[:max_sentences]
    return " ".join(selected)


def generate_description(clean_text, chapters):
    summary = generate_summary(clean_text)
    chapter_body = chapters.strip()
    if chapter_body == FALLBACK_MESSAGE:
        chapter_body = "Chapters can be added after reviewing the full video."

    lines = [
        "YouTube Description Draft",
        "",
        "Title:",
        "Add your final video title here",
        "",
        "Summary:",
        summary,
        "",
        "Chapters:",
        chapter_body,
        "",
        "Notes:",
        "- Review names, links, and calls to action before publishing.",
        "- Add your social links, credits, and relevant resources here.",
    ]
    return "\n".join(lines).strip() + "\n"


def score_snippet(sentence):
    score = 0
    lowered = sentence.lower()
    if "?" in sentence:
        score += 2
    if any(word in lowered for word in ["how", "why", "best", "important", "simple", "first", "today"]):
        score += 2
    length = len(sentence)
    if 45 <= length <= 150:
        score += 2
    elif length <= 180:
        score += 1
    return score


def generate_caption_snippets(text, limit=8):
    sentences = split_sentences(text)
    candidates = [
        sentence for sentence in sentences
        if 35 <= len(sentence) <= 180 and len(sentence.split()) >= 6
    ]
    ranked = sorted(candidates, key=score_snippet, reverse=True)

    snippets = []
    seen = set()
    for sentence in ranked:
        key = sentence.lower()
        if key in seen:
            continue
        seen.add(key)
        snippets.append(sentence)
        if len(snippets) >= limit:
            break

    if not snippets:
        return FALLBACK_MESSAGE + "\n"

    lines = ["Caption Snippets", ""]
    for index, snippet in enumerate(snippets, start=1):
        lines.append(f"{index}. {snippet}")
    return "\n".join(lines).strip() + "\n"


def generate_title_ideas(text, limit=8):
    topic = transcript_topic(text)
    keywords = extract_keywords(text, limit=8)
    focus = ", ".join(word.title() for word in keywords[:2]) or topic
    templates = [
        f"{topic}: What You Need to Know",
        f"How {topic} Changes the Way You Create",
        f"The Simple Guide to {topic}",
        f"What I Learned About {topic}",
        f"{topic} Explained Clearly",
        f"Before You Start With {topic}, Watch This",
        f"The Practical Way to Think About {topic}",
        f"{focus}: Key Takeaways and Next Steps",
    ]
    return numbered_section("Title Ideas", unique_items(templates, limit))


def generate_hook_ideas(text, limit=8):
    topic = transcript_topic(text)
    summary = generate_summary(text, max_sentences=1)
    templates = [
        f"If you care about {topic}, this is the part most people miss.",
        f"Here is the simplest way to understand {topic}.",
        f"This one idea can change how you think about {topic}.",
        f"Before you move forward, understand this about {topic}.",
        f"Most people overcomplicate {topic}. Let us make it clear.",
        f"The real value of {topic} starts with one practical step.",
        f"If you only take one thing from this, make it this: {summary}",
        f"Here is a creator-friendly breakdown of {topic}.",
    ]
    return numbered_section("Hook Ideas", unique_items(templates, limit))


def generate_platform_captions(text):
    topic = transcript_topic(text)
    summary = generate_summary(text, max_sentences=2)
    lines = [
        "Platform Captions",
        "",
        "YouTube:",
        f"{summary}\n\nIn this video, we break down {topic} with practical takeaways you can use. Watch, review the chapters, and share your thoughts in the comments.",
        "",
        "Instagram:",
        f"{topic} made simple.\n\n{summary}\n\nSave this for later and share it with someone who needs a clear breakdown.",
        "",
        "X/Twitter:",
        f"{topic} made practical: {summary}",
        "",
        "LinkedIn:",
        f"A practical look at {topic}.\n\n{summary}\n\nThe key takeaway: focus on clarity, useful next steps, and what the audience can apply immediately.",
    ]
    return "\n".join(lines).strip() + "\n"


def generate_clip_ideas(text, segments, limit=8):
    source_segments = [
        segment for segment in (segments or [])
        if segment_text(segment) and segment.get("start") is not None
    ]
    lines = ["Clip Ideas", ""]
    if source_segments:
        ranked = sorted(source_segments, key=lambda segment: score_snippet(segment_text(segment)), reverse=True)
        for index, segment in enumerate(ranked[:limit], start=1):
            text_value = segment_text(segment)
            start = format_hms(segment.get("start", 0))
            end = format_hms(segment.get("end", segment.get("start", 0)))
            title = choose_chapter_title(text_value)
            lines.extend(
                [
                    f"{index}. {title}",
                    f"Timestamp: {start} - {end}",
                    f"Why it works: {shorten_text(text_value, 140)}",
                    f"Suggested hook: {shorten_text(text_value, 90)}",
                    "",
                ]
            )
    else:
        candidates = sorted(split_sentences(text), key=score_snippet, reverse=True)[:limit]
        for index, sentence in enumerate(candidates, start=1):
            title = choose_chapter_title(sentence)
            lines.extend(
                [
                    f"{index}. {title}",
                    "Timestamp: Not available for pasted transcripts",
                    f"Why it works: {shorten_text(sentence, 140)}",
                    f"Suggested hook: {shorten_text(sentence, 90)}",
                    "",
                ]
            )
    if len(lines) == 2:
        return FALLBACK_MESSAGE + "\n"
    return "\n".join(lines).strip() + "\n"


def generate_pinned_comments(text, limit=5):
    topic = transcript_topic(text)
    templates = [
        f"What was your biggest takeaway from this breakdown of {topic}?",
        "If this helped, subscribe or follow for more practical creator-focused breakdowns.",
        "Links, resources, and extra notes can be added here before publishing.",
        f"Which part of {topic} should we go deeper on next?",
        "Drop your questions below. I will use the best ones for future content.",
    ]
    return numbered_section("Pinned Comment Options", unique_items(templates, limit))


def generate_hashtags_keywords(text):
    keywords = extract_keywords(text, limit=15)
    if not keywords:
        return FALLBACK_MESSAGE + "\n"
    hashtags = [f"#{to_hashtag(keyword)}" for keyword in keywords[:15]]
    phrases = build_search_phrases(keywords, transcript_topic(text), limit=10)
    lines = [
        "Hashtags and Keywords",
        "",
        "Keywords:",
        ", ".join(keywords),
        "",
        "Hashtags:",
        " ".join(hashtags),
        "",
        "Search Phrases:",
    ]
    lines.extend(f"{index}. {phrase}" for index, phrase in enumerate(phrases, start=1))
    return "\n".join(lines).strip() + "\n"


def generate_publish_pack(assets):
    sections = [
        "# Publish Pack",
        "",
        "## Quick Checklist",
        "- Review names, links, and claims.",
        "- Pick one title and one hook.",
        "- Copy the platform caption you need.",
        "- Add final links, credits, and calls to action.",
        "- Confirm captions and timestamps before publishing.",
        "",
        "## Title Ideas",
        strip_heading(assets["title_ideas"]),
        "",
        "## Hook Ideas",
        strip_heading(assets["hook_ideas"]),
        "",
        "## YouTube Description",
        strip_heading(assets["youtube_description"]),
        "",
        "## Chapters",
        strip_heading(assets["chapters"]),
        "",
        "## Platform Captions",
        strip_heading(assets["platform_captions"]),
        "",
        "## Clip Ideas",
        strip_heading(assets["clip_ideas"]),
        "",
        "## Pinned Comments",
        strip_heading(assets["pinned_comments"]),
        "",
        "## Hashtags and Keywords",
        strip_heading(assets["hashtags_keywords"]),
    ]
    return "\n".join(sections).strip() + "\n"


def unique_items(items, limit):
    result = []
    seen = set()
    for item in items:
        key = item.lower()
        if key in seen:
            continue
        seen.add(key)
        result.append(item)
        if len(result) >= limit:
            break
    return result


def numbered_section(title, items):
    if not items:
        return FALLBACK_MESSAGE + "\n"
    lines = [title, ""]
    lines.extend(f"{index}. {item}" for index, item in enumerate(items, start=1))
    return "\n".join(lines).strip() + "\n"


def shorten_text(text, limit):
    clean = normalize_spaces(text)
    if len(clean) <= limit:
        return clean
    return clean[: limit - 3].rstrip() + "..."


def to_hashtag(value):
    return re.sub(r"[^a-zA-Z0-9]", "", value.title()) or "Creator"


def build_search_phrases(keywords, topic, limit=10):
    bases = keywords[:5] or [topic]
    phrases = []
    for word in bases:
        phrases.extend(
            [
                f"{word} explained",
                f"how to use {word}",
            ]
        )
    phrases.append(f"{topic} key takeaways")
    return unique_items(phrases, limit)


def strip_heading(text):
    lines = (text or "").strip().splitlines()
    if len(lines) > 2 and lines[1].strip() == "":
        return "\n".join(lines[2:]).strip()
    return (text or "").strip()


def build_creator_assets(text, segments):
    clean = clean_transcript(text)
    chapters = generate_chapters(segments)
    snippets = generate_caption_snippets(clean)
    description = generate_description(clean, chapters)
    assets = {
        "clean_transcript": clean,
        "chapters": chapters,
        "youtube_description": description,
        "caption_snippets": snippets,
        "title_ideas": generate_title_ideas(clean),
        "hook_ideas": generate_hook_ideas(clean),
        "platform_captions": generate_platform_captions(clean),
        "clip_ideas": generate_clip_ideas(clean, segments),
        "pinned_comments": generate_pinned_comments(clean),
        "hashtags_keywords": generate_hashtags_keywords(clean),
    }
    assets["publish_pack"] = generate_publish_pack(assets)
    return assets
