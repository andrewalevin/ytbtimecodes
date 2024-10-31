# Timecode Processor

A Python library for extracting, cleaning, and standardizing timecodes within text. This tool is designed to parse timecodes in various formats (e.g., `MM:SS`, `HH:MM:SS`), and filter them based on specified time bounds.

## Features

- **Timecode Extraction**: Finds and extracts timecodes and associated titles from blocks of text.
- **Timecode Conversion**: Converts timecodes from string format to seconds or formatted `timedelta`.
- **Standardization**: Standardizes time formats to a clean, unified format.
- **Filtering**: Filters timecodes within specified time bounds.
- **Text Cleaning**: Cleans unwanted patterns and trims whitespace.

## Installation

```bash
pip install timecode-processor
```


```python
import logging
from timecode_processor import (
    clean_input_text,
    convert_time_to_seconds,
    locate_timecodes_block,
    extract_timecodes,
    filter_timecodes_within_bounds,
    standardize_time_format,
    timedelta_from_seconds
)

# Example input text
text = """
0:01 Intro
1:23 Overview
5:45 Deep Dive
10:00 Wrap Up
"""

# Extract and clean timecodes
timecodes = extract_timecodes(text)
print(timecodes)

# Filter timecodes within bounds (in seconds)
filtered_timecodes = filter_timecodes_within_bounds(timecodes, start_time=60, end_time=600)
print(filtered_timecodes)
```


# API Reference

timedelta_from_seconds(seconds: str) -> str

Converts seconds into a human-readable timedelta format.

standardize_time_format(time_str: str) -> str

Standardizes a time string format, converting values like 00:00:00 to 0:00.

clean_input_text(text: str) -> str

Removes unwanted patterns and extra whitespace from the input text.

convert_time_to_seconds(time_str: str) -> int

Converts a time string in MM:SS or HH:MM:SS format to an integer representing total seconds.

locate_timecodes_block(text: str) -> str

Locates blocks of text containing multiple timecodes.

extract_timecodes(text: str) -> list

Extracts timecodes and associated titles from text.

filter_timecodes_within_bounds(timecodes: list, start_time: int, end_time: int) -> list

Filters timecodes based on specified time bounds.



