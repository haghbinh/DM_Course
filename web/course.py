"""Course details shared by the website hook (hooks.py) and the PDF maker
(make_pdfs.py). Change them here only."""

import re

COURSE_TITLE = "داده‌کاوی"
COURSE_SUBTITLE = "جزوه‌های درس"
INSTRUCTOR = "دکتر حسین حق‌بین"
UNIVERSITY = "دانشگاه خلیج فارس"
BOOK = ""  # optional line on the PDF cover; empty = not shown
SITE_URL = "haghbinh.github.io/DM_Course"

# Session pages are the notes inside the Part folders
SESSION_PREFIX = "Part "

FA_DIGITS = str.maketrans("۰۱۲۳۴۵۶۷۸۹", "0123456789")


def is_session(src_uri):
    return src_uri.startswith(SESSION_PREFIX)


def pdf_name(src_uri):
    """PDF file name for a note, with ASCII names only:
    'Part 0_Introduction/۱ - مقدمه....md' -> 'session-01.pdf',
    'Part 3_.../پروژه 1- ....md'          -> 'project-1.pdf'."""
    stem = src_uri.rsplit("/", 1)[-1][:-3].translate(FA_DIGITS)
    m = re.match(r"\s*(\d+)", stem)
    if m:
        return f"session-{int(m.group(1)):02d}.pdf"
    m = re.match(r"\s*پروژه\s*(\d+)", stem)
    if m:
        return f"project-{int(m.group(1))}.pdf"
    return re.sub(r"[^\w-]+", "-", stem).strip("-") + ".pdf"


def split_label(label):
    """Nav label 'جلسه ۱: مقدمه‌ای بر داده‌کاوی' -> ('جلسه ۱', 'مقدمه‌ای بر داده‌کاوی')."""
    head, sep, topic = label.partition(":")
    return (head.strip(), topic.strip()) if sep else (label.strip(), "")
