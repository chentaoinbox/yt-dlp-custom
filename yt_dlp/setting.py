#!/usr/bin/env python3
"""
setting.py - 生成 yt-dlp 配置文件

使用方法：
    python setting.py                # 在当前目录创建 yt-dlp-config 文件夹并生成 config
    python setting.py /path/to/dir   # 在指定目录创建文件夹并生成 config
"""

import os
import sys
import os
import zipfile
import tarfile
import platform
from tqdm import tqdm
import requests
import shutil
from pathlib import Path


class ConfigGenerator:
    def __init__(self):
        self.basedir = self.get_base_path()
        # print(self.basedir)
        self.main()
        pass

    def generate_config(self,output_dir="config"):
        """
        生成 yt-dlp 配置文件
        
        Args:
            output_dir: 输出目录，默认为当前目录下的 "config" 文件夹
        """
        output_dir = os.path.join(self.basedir, output_dir)
        
        # 创建目录（如果不存在）
        os.makedirs(output_dir, exist_ok=True)
        
        # 配置文件路径（无扩展名）
        config_path = os.path.join(output_dir, "config")
        
        # =========================================================
        # 配置文件内容
        # =========================================================
        config_content = '''# coding: utf-8

# ============================================================================
# yt-dlp Default Configuration (shlex format)
# Generated from yt-dlp source code
# ============================================================================
# This file contains ALL available options with their default values
# To enable an option, remove the '#' at the beginning of the line
# ============================================================================


# ============================================================================
# GENERAL OPTIONS
# ============================================================================

# --help | -h
#   Print this help text and exit
#   Type: flag (no value)
# --version
#   Print program version and exit
#   Type: flag (no value)

# --update | -U
#   Update this program to the latest version
#   Type: flag (no value)
# --no-update
#   Do not check for updates (default)
#   Type: flag (no value)

# --update-to [CHANNEL]@[TAG]
#   Upgrade/downgrade to a specific version
#   Format: [CHANNEL]@[TAG] (CHANNEL and TAG default to "stable" and "latest")
#   Example: --update-to master@2023.01.01
#   Type: string

# --ignore-errors | -i
#   Ignore download and postprocessing errors
#   Type: flag (no value)
# --no-abort-on-error
#   Continue with next video on download errors (default)
#   Type: flag (no value)
# --abort-on-error
#   Abort downloading of further videos if an error occurs
#   Type: flag (no value)

# --list-extractors
#   List all supported extractors and exit
#   Type: flag (no value)
# --extractor-descriptions
#   Output descriptions of all supported extractors and exit
#   Type: flag (no value)

# --use-extractors | --ies NAMES
#   Extractor names to use separated by commas
#   Format: comma-separated list (supports regex, "all", "default", "end", "-" to exclude)
#   Example: --ies "holodex.*,end,youtube" or --ies default,-generic
#   Type: string
#   Default: []

# --default-search PREFIX
#   Use this prefix for unqualified URLs
#   Format: "auto", "auto_warning", "error", "fixup_error", or custom prefix like "gvsearch2:"
#   Default: "fixup_error"
#   Type: string

# --ignore-config | --no-config
#   Don't load any more configuration files except those given to --config-locations
#   Type: flag (no value)

# --config-locations PATH
#   Location of the main configuration file; either the path to the config or its containing directory ("-" for stdin)
#   Can be used multiple times
#   Type: path
--config-location config

# --plugin-dirs DIR
#   Path to an additional directory to search for plugins
#   Format: directory path, use "default" to search default plugin directories
#   Can be used multiple times
#   Type: path
#   Default: ['default']

# --js-runtimes RUNTIME[:PATH]
#   Additional JavaScript runtime to enable
#   Format: runtime[:path] (runtimes: deno, node, quickjs, bun)
#   Example: --js-runtimes deno:/usr/local/bin/deno
#   Can be used multiple times
#   Type: string
#   Default: ['deno']

# --remote-components COMPONENT
#   Remote components to allow yt-dlp to fetch when required
#   Format: ejs:npm or ejs:github
#   Can be used multiple times
#   Type: string
#   Default: []

# --flat-playlist
#   Do not extract a playlist's URL result entries; some entry metadata may be missing
#   Type: flag (no value)
# --no-flat-playlist
#   Fully extract the videos of a playlist (default)
#   Type: flag (no value)

# --live-from-start
#   Download livestreams from the start (experimental, YouTube/Twitch/TVer)
#   Type: flag (no value)
# --no-live-from-start
#   Download livestreams from the current time (default)
#   Type: flag (no value)

# --wait-for-video MIN[-MAX]
#   Wait for scheduled streams to become available
#   Format: number or range (e.g., 5 or 5-10)
#   Type: string

# --mark-watched
#   Mark videos watched (even with --simulate)
#   Type: flag (no value)
# --no-mark-watched
#   Do not mark videos watched (default)
#   Type: flag (no value)

# --color [STREAM:]POLICY
#   Whether to emit color codes in output
#   Format: [stdout|stderr:]always|auto|never|no_color|auto-tty|no_color-tty
#   Can be used multiple times
#   Example: --color stdout:always --color stderr:auto
#   Type: string
#   Default: {}

# --compat-options OPTS
#   Options that can help keep compatibility with youtube-dl or youtube-dlc
#   Format: comma-separated list of: filename, filename-sanitization, format-sort, abort-on-error,
#           format-spec, no-playlist-metafiles, multistreams, no-live-chat, playlist-index,
#           list-formats, no-direct-merge, playlist-match-filter, no-attach-info-json,
#           embed-thumbnail-atomicparsley, no-external-downloader-progress, embed-metadata,
#           seperate-video-versions, no-clean-infojson, no-keep-subs, no-certifi,
#           no-youtube-channel-redirect, no-youtube-unavailable-videos,
#           no-youtube-prefer-utc-upload-date, prefer-legacy-http-handler,
#           manifest-filesize-approx, allow-unsafe-ext, prefer-vp9-sort, mtime-by-default
#   Aliases: youtube-dl, youtube-dlc, 2021, 2022, 2023, 2024, 2025
#   Type: string
#   Default: set()

# --alias ALIASES OPTIONS
#   Create aliases for an option string
#   Format: aliases options (aliases: comma-separated, options: Python format string)
#   Example: --alias get-audio,-X "-S aext:{0},abr -x --audio-format {0}"
#   Type: string (nargs=2)

# --preset-alias | -t PRESET
#   Applies a predefined set of options
#   Available presets: mp3, aac, mp4, mkv, sleep
#   Type: string


# ============================================================================
# NETWORK OPTIONS
# ============================================================================

# --proxy URL
#   Use the specified HTTP/HTTPS/SOCKS proxy
#   Format: http://user:pass@host:port, socks5://user:pass@host:1080/, or "" for direct connection
#   Example: --proxy http://127.0.0.1:7890
#   Type: string

# --socket-timeout SECONDS
#   Time to wait before giving up, in seconds
#   Type: float
#   Default: None

# --source-address IP
#   Client-side IP address to bind to
#   Type: IP address

# --impersonate CLIENT[:OS]
#   Client to impersonate for requests
#   Format: chrome, chrome-110, chrome:windows-10, firefox, safari, edge, tor
#   Example: --impersonate chrome:windows-10
#   Type: string

# --list-impersonate-targets
#   List available clients to impersonate
#   Type: flag (no value)

# --force-ipv4 | -4
#   Make all connections via IPv4
#   Type: flag (no value)

# --force-ipv6 | -6
#   Make all connections via IPv6
#   Type: flag (no value)

# --enable-file-urls
#   Enable file:// URLs (disabled by default for security)
#   Type: flag (no value)


# ============================================================================
# GEO-RESTRICTION OPTIONS
# ============================================================================

# --geo-verification-proxy URL
#   Use this proxy to verify the IP address for some geo-restricted sites
#   Type: URL

# --xff VALUE
#   How to fake X-Forwarded-For HTTP header
#   Format: "default", "never", IP block in CIDR, or two-letter ISO 3166-2 country code
#   Example: --xff US or --xff 192.168.0.0/24
#   Default: "default"
#   Type: string


# ============================================================================
# VIDEO SELECTION OPTIONS
# ============================================================================

# --playlist-start NUMBER
#   Playlist video to start at (default is 1)
#   Type: integer
#   Default: 1

# --playlist-end NUMBER
#   Playlist video to end at
#   Type: integer
#   Default: None

# --playlist-items | -I ITEM_SPEC
#   Comma-separated playlist_index of the items to download
#   Format: [START]:[STOP][:STEP] or START-STOP (backward compatible)
#   Example: -I 1:3,7,-5::2
#   Type: string

# --min-filesize SIZE
#   Abort download if filesize is smaller than SIZE
#   Format: number with suffix (e.g., 50k, 44.6M)
#   Type: string

# --max-filesize SIZE
#   Abort download if filesize is larger than SIZE
#   Format: number with suffix (e.g., 50k, 44.6M)
#   Type: string

# --date DATE
#   Download only videos uploaded on this date
#   Format: YYYYMMDD, now, today, yesterday, or today-2weeks
#   Example: --date today-2weeks
#   Type: string

# --datebefore DATE
#   Download only videos uploaded on or before this date
#   Format: same as --date
#   Type: string

# --dateafter DATE
#   Download only videos uploaded on or after this date
#   Format: same as --date
#   Type: string

# --match-filters FILTER
#   Generic video filter
#   Format: field operators: =, !=, ^=, $=, *=, ~=, >, <, >=, <=, >?, <?
#   Use "&" to combine, "\" to escape
#   Example: !is_live or "like_count>?100 & description~='(?i)\\bcats \\& dogs\\b'"
#   Use "--match-filters -" for interactive mode
#   Can be used multiple times (OR logic)
#   Type: string

# --break-match-filters FILTER
#   Same as --match-filters but stops the download process when a video is rejected
#   Type: string

# --no-playlist
#   Download only the video, if the URL refers to a video and a playlist
#   Type: flag (no value)
# --yes-playlist
#   Download the playlist, if the URL refers to a video and a playlist
#   Type: flag (no value)

# --age-limit YEARS
#   Download only videos suitable for the given age
#   Type: integer

# --download-archive FILE
#   Download only videos not listed in the archive file
#   Format: file path
#   Type: string

# --max-downloads NUMBER
#   Abort after downloading NUMBER files
#   Type: integer

# --break-on-existing
#   Stop the download process when encountering a file that is in the archive
#   Type: flag (no value)

# --break-per-input
#   Alters --max-downloads, --break-on-existing, --break-match-filters, and autonumber to reset per input URL
#   Type: flag (no value)

# --skip-playlist-after-errors N
#   Number of allowed failures until the rest of the playlist is skipped
#   Type: integer


# ============================================================================
# AUTHENTICATION OPTIONS
# ============================================================================

# --username | -u USERNAME
#   Login with this account ID
#   Type: string

# --password | -p PASSWORD
#   Account password (will ask interactively if omitted)
#   Type: string

# --twofactor | -2 TWOFACTOR
#   Two-factor authentication code
#   Type: string

# --netrc | -n
#   Use .netrc authentication data
#   Type: flag (no value)

# --netrc-location PATH
#   Location of .netrc authentication data; either the path or its containing directory
#   Default: ~/.netrc
#   Type: path

# --netrc-cmd NETRC_CMD
#   Command to execute to get the credentials for an extractor
#   Type: string

# --video-password PASSWORD
#   Video-specific password
#   Type: string

# --ap-mso MSO
#   Adobe Pass multiple-system operator (TV provider) identifier
#   Use --ap-list-mso for a list
#   Type: string

# --ap-username USERNAME
#   Multiple-system operator account login
#   Type: string

# --ap-password PASSWORD
#   Multiple-system operator account password (will ask interactively if omitted)
#   Type: string

# --ap-list-mso
#   List all supported multiple-system operators
#   Type: flag (no value)

# --client-certificate CERTFILE
#   Path to client certificate file in PEM format
#   Type: path

# --client-certificate-key KEYFILE
#   Path to private key file for client certificate
#   Type: path

# --client-certificate-password PASSWORD
#   Password for client certificate private key, if encrypted
#   Type: string


# ============================================================================
# VIDEO FORMAT OPTIONS
# ============================================================================

# --format | -f FORMAT
#   Video format code
#   Format: format specifier (e.g., "best", "bestvideo+bestaudio", "22", "best[height<=1080]")
#   See "FORMAT SELECTION" in documentation
#   Type: string
--format best[height<=1080]+bestaudio

# --format-sort | -S SORTORDER
#   Sort the formats by the fields given
#   Format: comma-separated fields with optional prefixes: + (ascending), - (descending)
#   Example: -S res,codec:av1, -S +bitrate,-fps
#   Type: string (can be used multiple times)
#   Default: []

# --format-sort-force | --S-force
#   Force user specified sort order to have precedence over all fields
#   Type: flag (no value)

# --video-multistreams
#   Allow multiple video streams to be merged into a single file
#   Type: flag (no value)
# --no-video-multistreams
#   Only one video stream is downloaded for each output file (default)
#   Type: flag (no value)

# --audio-multistreams
#   Allow multiple audio streams to be merged into a single file
#   Type: flag (no value)
# --no-audio-multistreams
#   Only one audio stream is downloaded for each output file (default)
#   Type: flag (no value)

# --prefer-free-formats
#   Prefer video formats with free containers over non-free ones of the same quality
#   Type: flag (no value)

# --check-formats
#   Make sure formats are selected only from those that are actually downloadable
#   Type: flag (no value)
# --check-all-formats
#   Check all formats for whether they are actually downloadable
#   Type: flag (no value)

# --list-formats | -F
#   List available formats of each video
#   Type: flag (no value)

# --merge-output-format FORMAT
#   Containers that may be used when merging formats, separated by "/"
#   Supported: mp4, mkv, webm, flv, avi, mov, ogg, etc.
#   Example: --merge-output-format mp4/mkv
#   Type: string
--merge-output-format mp4

# ============================================================================
# SUBTITLE OPTIONS
# ============================================================================

# --write-subs | --write-srt
#   Write subtitle file
#   Type: flag (no value)

# --write-auto-subs | --write-automatic-subs
#   Write automatically generated subtitle file
#   Type: flag (no value)

# --list-subs
#   List available subtitles of each video
#   Type: flag (no value)

# --sub-format FORMAT
#   Subtitle format; accepts formats preference separated by "/"
#   Supported: srt, ass, vtt, ttml, best
#   Example: --sub-format ass/srt/best
#   Default: "best"
#   Type: string

# --sub-langs | --srt-langs LANGS
#   Languages of the subtitles to download (can be regex) or "all"
#   Format: comma-separated language codes, prefix with "-" to exclude
#   Example: --sub-langs "en.*,ja,-live_chat"
#   Type: string
#   Default: []


# ============================================================================
# DOWNLOAD OPTIONS
# ============================================================================

# --concurrent-fragments | -N N
#   Number of fragments of a dash/hlsnative video that should be downloaded concurrently
#   Default: 1
#   Type: integer

# --limit-rate | -r RATE
#   Maximum download rate in bytes per second
#   Format: number with suffix (e.g., 50K, 4.2M)
#   Type: string

# --throttled-rate RATE
#   Minimum download rate in bytes per second below which throttling is assumed
#   Format: number with suffix (e.g., 100K)
#   Type: string

# --retries | -R RETRIES
#   Number of retries (default is 10), or "infinite"
#   Default: 10
#   Type: string (integer or "infinite")

# --file-access-retries RETRIES
#   Number of times to retry on file access error (default is 3), or "infinite"
#   Default: 3
#   Type: string

# --fragment-retries RETRIES
#   Number of retries for a fragment (default is 10), or "infinite"
#   Default: 10
#   Type: string

# --retry-sleep [TYPE:]EXPR
#   Time to sleep between retries in seconds
#   Format: [http|fragment|file_access|extractor:]number or linear=START[:END[:STEP]] or exp=START[:END[:BASE]]
#   Example: --retry-sleep linear=1::2 --retry-sleep fragment:exp=1:20
#   Type: string
#   Default: {}

# --skip-unavailable-fragments
#   Skip unavailable fragments for DASH, hlsnative and ISM downloads (default)
#   Type: flag (no value)
# --abort-on-unavailable-fragments
#   Abort download if a fragment is unavailable
#   Type: flag (no value)

# --keep-fragments
#   Keep downloaded fragments on disk after downloading is finished
#   Type: flag (no value)

# --buffer-size SIZE
#   Size of download buffer
#   Format: number with suffix (e.g., 1024, 16K)
#   Default: "1024"
#   Type: string

# --resize-buffer
#   The buffer size is automatically resized from an initial value of --buffer-size (default)
#   Type: flag (no value)
# --no-resize-buffer
#   Do not automatically adjust the buffer size
#   Type: flag (no value)

# --http-chunk-size SIZE
#   Size of a chunk for chunk-based HTTP downloading
#   Format: number with suffix (e.g., 10M)
#   Default: disabled
#   Type: string

# --playlist-random
#   Download playlist videos in random order
#   Type: flag (no value)

# --lazy-playlist
#   Process entries in the playlist as they are received
#   Type: flag (no value)

# --hls-use-mpegts
#   Use the mpegts container for HLS videos
#   Type: flag (no value)

# --download-sections REGEX
#   Download only chapters that match the regular expression
#   Format: regex, "*" prefix for time-range (e.g., "*10:15-inf"), "*from-url"
#   Can be used multiple times
#   Type: string

# --downloader | --external-downloader [PROTO:]NAME
#   Name or path of the external downloader to use
#   Format: [http|ftp|m3u8|dash|rtsp|rtmp|mms:]name
#   Supported: native, aria2c, wget, curl, httpie
#   Example: --downloader aria2c --downloader "dash,m3u8:native"
#   Type: string
#   Default: {}

# --downloader-args | --external-downloader-args NAME:ARGS
#   Give these arguments to the external downloader
#   Format: downloader_name:args (args are split by shlex)
#   Example: --downloader-args aria2c:"-x 16 -k 1M"
#   Type: string
#   Default: {}


# ============================================================================
# FILESYSTEM OPTIONS
# ============================================================================

# --batch-file | -a FILE
#   File containing URLs to download ("-" for stdin), one URL per line
#   Type: path

# --paths | -P [TYPES:]PATH
#   The paths where the files should be downloaded
#   Format: [home|temp|default|subtitle|thumbnail|description|infojson|annotation|link|pl_infojson:]path
#   Example: -P "home:~/Videos" -P "temp:~/tmp"
#   Type: string
#   Default: {}

# --output | -o [TYPES:]TEMPLATE
#   Output filename template
#   Format: [default|subtitle|thumbnail|description|infojson|annotation|link|pl_thumbnail|pl_description|pl_infojson|chapter:]template
#   Variables: %(title)s, %(id)s, %(uploader)s, %(upload_date)s, %(ext)s, etc.
#   Example: -o "%(title)s.%(ext)s" or -o "playlist/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s"
#   Type: string
#   Default: {}

# --output-na-placeholder TEXT
#   Placeholder for unavailable fields in --output
#   Default: "NA"
#   Type: string
--output-na-placeholder ""

# --restrict-filenames
#   Restrict filenames to only ASCII characters, and avoid "&" and spaces in filenames
#   Type: flag (no value)

# --windows-filenames
#   Force filenames to be Windows-compatible
#   Type: flag (no value)

# --trim-filenames LENGTH
#   Limit the filename length (excluding extension) to the specified number of characters
#   Type: integer
#   Default: 0

# --no-overwrites | -w
#   Do not overwrite any files
#   Type: flag (no value)
# --force-overwrites
#   Overwrite all video and metadata files
#   Type: flag (no value)

# --continue | -c
#   Resume partially downloaded files/fragments (default)
#   Type: flag (no value)
# --no-continue
#   Do not resume partially downloaded fragments
#   Type: flag (no value)

# --part
#   Use .part files instead of writing directly into output file (default)
#   Type: flag (no value)
# --no-part
#   Do not use .part files - write directly into output file
#   Type: flag (no value)

# --mtime
#   Use the Last-modified header to set the file modification time
#   Type: flag (no value)

# --write-description
#   Write video description to a .description file
#   Type: flag (no value)

# --write-info-json
#   Write video metadata to a .info.json file (may contain personal information)
#   Type: flag (no value)

# --write-playlist-metafiles
#   Write playlist metadata in addition to the video metadata (default)
#   Type: flag (no value)

# --clean-info-json
#   Remove some internal metadata such as filenames from the infojson (default)
#   Type: flag (no value)

# --write-comments | --get-comments
#   Retrieve video comments to be placed in the infojson
#   Type: flag (no value)

# --load-info-json FILE
#   JSON file containing the video information (created with --write-info-json)
#   Type: path

# --cookies FILE
#   Netscape formatted file to read cookies from and dump cookie jar in
#   Type: path
--cookies cookies/cookies.txt

# --cookies-from-browser BROWSER[+KEYRING][:PROFILE][::CONTAINER]
#   The name of the browser to load cookies from
#   Supported browsers: chrome, chromium, firefox, brave, edge, opera, safari, etc.
#   Supported keyrings: kwallet, gnomekeyring, libsecret, basic
#   Example: --cookies-from-browser firefox::default
#   Type: string

# --cache-dir DIR
#   Location in the filesystem where yt-dlp can store some downloaded information permanently
#   Default: ${XDG_CACHE_HOME}/yt-dlp
#   Type: path

# --rm-cache-dir
#   Delete all filesystem cache files
#   Type: flag (no value)


# ============================================================================
# THUMBNAIL OPTIONS
# ============================================================================

# --write-thumbnail
#   Write thumbnail image to disk
#   Type: flag (no value)

# --write-all-thumbnails
#   Write all thumbnail image formats to disk
#   Type: flag (no value)

# --list-thumbnails
#   List available thumbnails of each video
#   Type: flag (no value)


# ============================================================================
# INTERNET SHORTCUT OPTIONS
# ============================================================================

# --write-link
#   Write an internet shortcut file (.url, .webloc or .desktop)
#   Type: flag (no value)

# --write-url-link
#   Write a .url Windows internet shortcut
#   Type: flag (no value)

# --write-webloc-link
#   Write a .webloc macOS internet shortcut
#   Type: flag (no value)

# --write-desktop-link
#   Write a .desktop Linux internet shortcut
#   Type: flag (no value)


# ============================================================================
# VERBOSITY AND SIMULATION OPTIONS
# ============================================================================

# --quiet | -q
#   Activate quiet mode
#   Type: flag (no value)

# --no-warnings
#   Ignore warnings
#   Type: flag (no value)

# --simulate | -s
#   Do not download the video and do not write anything to disk
#   Type: flag (no value)

# --ignore-no-formats-error
#   Ignore "No video formats" error
#   Type: flag (no value)

# --skip-download | --no-download
#   Do not download the video but write all related files
#   Type: flag (no value)

# --print | -O [WHEN:]TEMPLATE
#   Field name or output template to print to screen
#   WHEN values: pre_process, after_filter, video, before_dl, post_process, after_move, after_video, playlist
#   Example: -O "%(title)s" or -O "playlist:%(playlist_title)s"
#   Type: string
#   Default: {}

# --print-to-file [WHEN:]TEMPLATE FILE
#   Append given template to the file
#   Type: string (nargs=2)
#   Default: {}

# --dump-json | -j
#   Quiet, but print JSON information for each video
#   Type: flag (no value)

# --dump-single-json | -J
#   Quiet, but print JSON information for each URL or infojson passed
#   Type: flag (no value)

# --force-write-archive
#   Force download archive entries to be written as far as no errors occur
#   Type: flag (no value)

# --newline
#   Output progress bar as new lines
#   Type: flag (no value)

# --no-progress
#   Do not print progress bar
#   Type: flag (no value)
# --progress
#   Show progress bar, even if in quiet mode
#   Type: flag (no value)

# --console-title
#   Display progress in console titlebar
#   Type: flag (no value)

# --progress-template [TYPES:]TEMPLATE
#   Template for progress outputs
#   Types: download, download-title, postprocess, postprocess-title
#   Variables: %(info.id)s, %(progress.eta)s, etc.
#   Example: --progress-template "download-title:%(info.id)s-%(progress.eta)s"
#   Type: string
#   Default: {}

# --progress-delta SECONDS
#   Time between progress output (default: 0)
#   Type: float
#   Default: 0

# --verbose | -v
#   Print various debugging information
#   Type: flag (no value)

# --dump-pages
#   Print downloaded pages encoded using base64 to debug problems
#   Type: flag (no value)

# --write-pages
#   Write downloaded intermediary pages to files in the current directory
#   Type: flag (no value)

# --print-traffic
#   Display sent and read HTTP traffic
#   Type: flag (no value)


# ============================================================================
# WORKAROUNDS
# ============================================================================

# --encoding ENCODING
#   Force the specified encoding (experimental)
#   Type: string

# --legacy-server-connect
#   Explicitly allow HTTPS connection to servers that do not support RFC 5746 secure renegotiation
#   Type: flag (no value)

# --no-check-certificates
#   Suppress HTTPS certificate validation
#   Type: flag (no value)

# --prefer-insecure | --prefer-unsecure
#   Use an unencrypted connection to retrieve information about the video
#   Type: flag (no value)

# --add-headers FIELD:VALUE
#   Specify a custom HTTP header and its value
#   Example: --add-headers "User-Agent:Mozilla/5.0" --add-headers "Accept-Language:zh-CN"
#   Type: string
#   Default: {}

# --bidi-workaround
#   Work around terminals that lack bidirectional text support
#   Type: flag (no value)

# --sleep-requests SECONDS
#   Number of seconds to sleep between requests during data extraction
#   Type: float

# --sleep-interval | --min-sleep-interval SECONDS
#   Number of seconds to sleep before each download
#   Type: float

# --max-sleep-interval SECONDS
#   Maximum number of seconds to sleep (only with --min-sleep-interval)
#   Type: float

# --sleep-subtitles SECONDS
#   Number of seconds to sleep before each subtitle download
#   Type: float
#   Default: 0


# ============================================================================
# POST-PROCESSING OPTIONS
# ============================================================================

# --extract-audio | -x
#   Convert video files to audio-only files (requires ffmpeg)
#   Type: flag (no value)

# --audio-format FORMAT
#   Format to convert the audio to when -x is used
#   Supported: best, mp3, m4a, aac, flac, opus, vorbis, wav
#   Example: --audio-format mp3
#   Default: "best"
#   Type: string

# --audio-quality QUALITY
#   Specify ffmpeg audio quality to use when converting the audio with -x
#   Format: 0-10 (VBR) or specific bitrate like 128K
#   Default: "5"
#   Type: string

# --remux-video FORMAT
#   Remux the video into another container if necessary
#   Supported: mp4, mkv, webm, flv, avi, mov, ogg
#   Example: --remux-video mp4
#   Type: string

# --recode-video FORMAT
#   Re-encode the video into another format if necessary
#   Format: same as --remux-video
#   Type: string

# --postprocessor-args | --ppa NAME:ARGS
#   Give these arguments to the postprocessors
#   Format: postprocessor_name[:executable]:args
#   Supported PP: Merger, ModifyChapters, SplitChapters, ExtractAudio, VideoRemuxer, VideoConvertor,
#                 Metadata, EmbedSubtitle, EmbedThumbnail, SubtitlesConvertor, ThumbnailsConvertor,
#                 FixupStretched, FixupM4a, FixupM3u8, FixupTimestamp, FixupDuration
#   Example: --ppa "Merger+ffmpeg_i1:-v quiet" or --ppa "ExtractAudio:-acodec mp3 -ab 192k"
#   Type: string
#   Default: {}

# --keep-video | -k
#   Keep the intermediate video file on disk after post-processing
#   Type: flag (no value)

# --post-overwrites
#   Overwrite post-processed files (default)
#   Type: flag (no value)
# --no-post-overwrites
#   Do not overwrite post-processed files
#   Type: flag (no value)

# --embed-subs
#   Embed subtitles in the video (only for mp4, webm and mkv videos)
#   Type: flag (no value)

# --embed-thumbnail
#   Embed thumbnail in the video as cover art
#   Type: flag (no value)

# --embed-metadata | --add-metadata
#   Embed metadata to the video file. Also embeds chapters/infojson if present
#   Type: flag (no value)

# --embed-chapters | --add-chapters
#   Add chapter markers to the video file
#   Type: flag (no value)

# --embed-info-json
#   Embed the infojson as an attachment to mkv/mka video files
#   Type: flag (no value)

# --xattrs | --xattr
#   Write metadata to the video file's xattrs (using Dublin Core and XDG standards)
#   Type: flag (no value)

# --concat-playlist POLICY
#   Concatenate videos in a playlist
#   Values: never, always, multi_video (default)
#   Default: "multi_video"
#   Type: string

# --fixup POLICY
#   Automatically correct known faults of the file
#   Values: never, ignore, warn, detect_or_warn, force
#   Type: string

# --ffmpeg-location PATH
#   Location of the ffmpeg binary; either the path to the binary or its containing directory
#   Type: path

# --exec [WHEN:]CMD
#   Execute a command
#   WHEN values: pre_process, after_filter, video, before_dl, post_process, after_move, after_video, playlist
#   Example: --exec "ffmpeg -i {} -c copy {}.mkv" or --exec "after_move:mv {} ~/Videos/"
#   Type: string
#   Default: {}

# --convert-subs | --convert-subtitles FORMAT
#   Convert the subtitles to another format
#   Supported: srt, ass, vtt, ttml, best
#   Type: string

# --convert-thumbnails FORMAT
#   Convert the thumbnails to another format
#   Supported: jpg, png, webp
#   Type: string

# --split-chapters | --split-tracks
#   Split video into multiple files based on internal chapters
#   Type: flag (no value)

# --remove-chapters REGEX
#   Remove chapters whose title matches the given regular expression
#   Format: same as --download-sections
#   Type: string

# --force-keyframes-at-cuts
#   Force keyframes at cuts when downloading/splitting/removing sections
#   Type: flag (no value)

# --use-postprocessor NAME[:ARGS]
#   The (case-sensitive) name of plugin postprocessors to be enabled
#   Format: name[:args] where args are semicolon-separated NAME=VALUE
#   Example: --use-postprocessor SponsorBlock:when=pre_process;key=value
#   Type: string
#   Default: []


# ============================================================================
# SPONSORBLOCK OPTIONS
# ============================================================================

# --sponsorblock-mark CATS
#   SponsorBlock categories to create chapters for
#   Categories: sponsor, intro, outro, selfpromo, preview, filler, interaction, music_offtopic, poi_highlight
#   Example: --sponsorblock-mark all,-preview
#   Type: string
#   Default: set()

# --sponsorblock-remove CATS
#   SponsorBlock categories to be removed from the video file
#   Categories: sponsor, intro, outro, selfpromo, preview, filler, interaction, music_offtopic
#   Example: --sponsorblock-remove all,-filler
#   Type: string
#   Default: set()

# --sponsorblock-chapter-title TEMPLATE
#   An output template for the title of the SponsorBlock chapters
#   Available fields: start_time, end_time, category, categories, name, category_names
#   Default: "[SponsorBlock]: %(category_names)s"
#   Type: string

# --sponsorblock-api URL
#   SponsorBlock API location
#   Default: "https://sponsor.ajay.app"
#   Type: string


# ============================================================================
# EXTRACTOR OPTIONS
# ============================================================================

# --extractor-retries RETRIES
#   Number of retries for known extractor errors
#   Default: 3
#   Type: string (integer or "infinite")

# --allow-dynamic-mpd
#   Process dynamic DASH manifests (default)
#   Type: flag (no value)
# --ignore-dynamic-mpd
#   Do not process dynamic DASH manifests
#   Type: flag (no value)

# --hls-split-discontinuity
#   Split HLS playlists to different formats at discontinuities such as ad breaks
#   Type: flag (no value)

# --extractor-args IE_KEY:ARGS
#   Pass ARGS arguments to the IE_KEY extractor
#   Format: extractor_key:arg1=value1;arg2=value2
#   Example: --extractor-args "youtube:skip=dash,lang=en" or --extractor-args "twitch:video_codec=h264"
#   Type: string
#   Default: {}


# ============================================================================
# End of configuration
# ============================================================================
'''
        
        # 写入文件
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write(config_content)
        return config_path

    def download_with_progress(self,url, dest, desc=None):
        try:
            if desc is None:
                desc = f"Download {os.path.basename(dest)}"
            response = requests.get(url, stream=True)
            response.raise_for_status()  # 检查请求是否成功
            total_size = int(response.headers.get('content-length', 0))
            with open(dest, 'wb') as file, tqdm(
                desc=desc,
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
                miniters=1,
                leave=False,
            ) as pbar:
                for data in response.iter_content(chunk_size=8192):
                    size = file.write(data)
                    pbar.update(size)
            return True
        except Exception as e:
            print(f"Download failed: {e}")
            return False

    def setffmpeg(self):
        """Install FFmpeg to basedir/ffmpeg directory"""
        system = platform.system().lower()
        arch = platform.machine().lower()
        
        # Use Path for absolute path handling
        basedir = Path(self.basedir).resolve()
        target_dir = basedir / "ffmpeg"
        zip_path = basedir / "ffmpeg.zip"
        
        try:
            if system == "windows":
                url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
                
                if not self.download_with_progress(url, str(zip_path), "Download FFmpeg"):
                    return None
                
                print("Extracting FFmpeg...")
                
                # Extract to temporary directory
                extract_dir = basedir / "ffmpeg_temp"
                if extract_dir.exists():
                    shutil.rmtree(extract_dir)
                extract_dir.mkdir(parents=True, exist_ok=True)
                
                with zipfile.ZipFile(zip_path, 'r') as zf:
                    zf.extractall(extract_dir)
                
                # Find the extracted folder
                extracted_folder = None
                for item in extract_dir.iterdir():
                    if item.is_dir() and item.name.startswith("ffmpeg"):
                        extracted_folder = item
                        break
                
                if extracted_folder:
                    # Remove old ffmpeg directory if exists
                    if target_dir.exists():
                        shutil.rmtree(target_dir)
                    # Move extracted content to target directory
                    shutil.move(str(extracted_folder), str(target_dir))
                else:
                    print("FFmpeg directory not found")
                    return None
                
                # Cleanup
                zip_path.unlink()
                shutil.rmtree(extract_dir)
                
                print(f"FFmpeg installation completed! -> {target_dir}")
                return str(target_dir)
            
            elif system == "linux":
                # Determine download URL
                if arch in ["x86_64", "amd64"]:
                    url = "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz"
                elif arch in ["aarch64", "arm64"]:
                    url = "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-arm64-static.tar.xz"
                else:
                    url = "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-armhf-static.tar.xz"
                
                tar_path = basedir / "ffmpeg.tar.xz"
                
                if not self.download_with_progress(url, str(tar_path), "Download FFmpeg"):
                    return None
                
                print("Extracting FFmpeg...")
                
                extract_dir = basedir / "ffmpeg_temp"
                if extract_dir.exists():
                    shutil.rmtree(extract_dir)
                extract_dir.mkdir(parents=True, exist_ok=True)
                
                with tarfile.open(tar_path, 'r:xz') as tf:
                    tf.extractall(extract_dir)
                
                # Find the extracted folder
                extracted_folder = None
                for item in extract_dir.iterdir():
                    if item.is_dir() and item.name.startswith("ffmpeg"):
                        extracted_folder = item
                        break
                
                if extracted_folder:
                    if target_dir.exists():
                        shutil.rmtree(target_dir)
                    shutil.move(str(extracted_folder), str(target_dir))
                    
                    # Set executable permissions
                    ffmpeg_bin = target_dir / "ffmpeg"
                    if ffmpeg_bin.exists():
                        ffmpeg_bin.chmod(0o755)
                else:
                    print("FFmpeg directory not found")
                    return None
                
                tar_path.unlink()
                shutil.rmtree(extract_dir)
                
                print(f"FFmpeg installation completed! -> {target_dir}")
                return str(target_dir)
            
            elif system == "darwin":  # macOS
                arch = "arm64" if arch == "arm64" else "intel"
                url = f"https://www.osxexperts.net/ffmpeg{arch}.zip"
                
                zip_path = basedir / "ffmpeg.zip"
                
                if not self.download_with_progress(url, str(zip_path), "Download FFmpeg"):
                    return None
                
                print("Extracting FFmpeg...")
                
                extract_dir = basedir / "ffmpeg_temp"
                if extract_dir.exists():
                    shutil.rmtree(extract_dir)
                extract_dir.mkdir(parents=True, exist_ok=True)
                
                with zipfile.ZipFile(zip_path, 'r') as zf:
                    zf.extractall(extract_dir)
                
                # Find the extracted folder
                extracted_folder = None
                for item in extract_dir.iterdir():
                    if item.is_dir() and item.name.startswith("ffmpeg"):
                        extracted_folder = item
                        break
                
                if extracted_folder:
                    if target_dir.exists():
                        shutil.rmtree(target_dir)
                    shutil.move(str(extracted_folder), str(target_dir))
                    
                    # Set executable permissions
                    ffmpeg_bin = target_dir / "ffmpeg"
                    if ffmpeg_bin.exists():
                        ffmpeg_bin.chmod(0o755)
                else:
                    print("FFmpeg directory not found")
                    return None
                
                zip_path.unlink()
                shutil.rmtree(extract_dir)
                
                print(f"FFmpeg installation completed! -> {target_dir}")
                return str(target_dir)
            
            return None
        
        except Exception as e:
            print(f"FFmpeg installation failed: {e}")
            return None

    def setnodejs(self):
        """Install Node.js to basedir/node directory"""
        system = platform.system().lower()
        arch = platform.machine().lower()
        version = "22.14.0"
        
        # Use Path for absolute path handling
        basedir = Path(self.basedir).resolve()
        target_dir = basedir / "node"
        
        try:
            if system == "windows":
                zip_path = basedir / "node.zip"
                url = f"https://nodejs.org/dist/v{version}/node-v{version}-win-x64.zip"
                
                if not self.download_with_progress(url, str(zip_path), f"Download Node.js {version}"):
                    return None
                
                print("Extracting Node.js...")
                
                extract_dir = basedir / "node_temp"
                if extract_dir.exists():
                    shutil.rmtree(extract_dir)
                extract_dir.mkdir(parents=True, exist_ok=True)
                
                with zipfile.ZipFile(zip_path, 'r') as zf:
                    zf.extractall(extract_dir)
                
                # Find the extracted folder
                extracted_folder = None
                for item in extract_dir.iterdir():
                    if item.is_dir() and item.name.startswith("node-v"):
                        extracted_folder = item
                        break
                
                if extracted_folder:
                    if target_dir.exists():
                        shutil.rmtree(target_dir)
                    shutil.move(str(extracted_folder), str(target_dir))
                else:
                    print("Node.js directory not found")
                    return None
                
                # Cleanup
                zip_path.unlink()
                shutil.rmtree(extract_dir)
                
                node_exe = target_dir / "node.exe"
                if node_exe.exists():
                    print(f"Node.js installation completed! -> {target_dir}")
                    return str(target_dir)
                else:
                    print("node.exe not found")
                    return None
            
            elif system == "linux":
                if arch in ["x86_64", "amd64"]:
                    filename = f"node-v{version}-linux-x64.tar.xz"
                elif arch in ["aarch64", "arm64"]:
                    filename = f"node-v{version}-linux-arm64.tar.xz"
                else:
                    filename = f"node-v{version}-linux-armv7l.tar.xz"
                
                url = f"https://nodejs.org/dist/v{version}/{filename}"
                tar_path = basedir / filename
                
                if not self.download_with_progress(url, str(tar_path), f"Download Node.js {version}"):
                    return None
                
                print("Extracting Node.js...")
                
                extract_dir = basedir / "node_temp"
                if extract_dir.exists():
                    shutil.rmtree(extract_dir)
                extract_dir.mkdir(parents=True, exist_ok=True)
                
                with tarfile.open(tar_path, 'r:xz') as tf:
                    tf.extractall(extract_dir)
                
                # Find the extracted folder
                extracted_folder = None
                for item in extract_dir.iterdir():
                    if item.is_dir() and item.name.startswith("node-v"):
                        extracted_folder = item
                        break
                
                if extracted_folder:
                    if target_dir.exists():
                        shutil.rmtree(target_dir)
                    shutil.move(str(extracted_folder), str(target_dir))
                    
                    # Set executable permissions
                    node_bin = target_dir / "bin" / "node"
                    if node_bin.exists():
                        node_bin.chmod(0o755)
                else:
                    print("Node.js directory not found")
                    return None
                
                tar_path.unlink()
                shutil.rmtree(extract_dir)
                
                print(f"Node.js installation completed! -> {target_dir}")
                return str(target_dir)
            
            elif system == "darwin":  # macOS
                arch = "arm64" if arch == "arm64" else "x64"
                filename = f"node-v{version}-darwin-{arch}.tar.gz"
                url = f"https://nodejs.org/dist/v{version}/{filename}"
                tar_path = basedir / filename
                
                if not self.download_with_progress(url, str(tar_path), f"Download Node.js {version}"):
                    return None
                
                print("Extracting Node.js...")
                
                extract_dir = basedir / "node_temp"
                if extract_dir.exists():
                    shutil.rmtree(extract_dir)
                extract_dir.mkdir(parents=True, exist_ok=True)
                
                with tarfile.open(tar_path, 'r:gz') as tf:
                    tf.extractall(extract_dir)
                
                # Find the extracted folder
                extracted_folder = None
                for item in extract_dir.iterdir():
                    if item.is_dir() and item.name.startswith("node-v"):
                        extracted_folder = item
                        break
                
                if extracted_folder:
                    if target_dir.exists():
                        shutil.rmtree(target_dir)
                    shutil.move(str(extracted_folder), str(target_dir))
                    
                    # Set executable permissions
                    node_bin = target_dir / "bin" / "node"
                    if node_bin.exists():
                        node_bin.chmod(0o755)
                else:
                    print("Node.js directory not found")
                    return None
                
                tar_path.unlink()
                shutil.rmtree(extract_dir)
                
                print(f"Node.js installation completed! -> {target_dir}")
                return str(target_dir)
            
            return None
        
        except Exception as e:
            print(f"Node.js installation failed: {e}")
            return None
    
    def configupdate(self, lines, target, message, way):
        target_index = None
        
        for i, line in enumerate(lines):
            if message in line:
                return lines
        
        for i, line in enumerate(lines):
            if target in line:
                target_index = i
                break

        if target_index is None:
            return lines
        
        if way == "insert":
            lines.insert(target_index - 1, f"{message}\n")
            return lines
        elif way == "replace":
            lines[target_index] = f"{message}\n"
            return lines
        return lines



    def check_ffmpeg(self):
        folder = ""
        folder = os.path.join(self.basedir, folder,"ffmpeg")
        return os.path.exists(folder)


    def check_nodejs(self):
        folder = ""
        folder = os.path.join(self.basedir, "node")
        return os.path.exists(folder)

    def checkconfig(self):
        config_path = ""
        config_path = os.path.join(self.basedir, "config", "config")
        return os.path.exists(config_path)
    
    def checkcookies(self):
        file = ""
        file = os.path.join(self.basedir, "cookies", "cookies.txt")
        return os.path.exists(file)
    
    def create_cookies(self):
        folder = ""
        folder = os.path.join(self.basedir, "cookies")
        # print(folder)
        if not os.path.exists(folder):
            os.makedirs(folder)

    def get_base_path(self):
        filedirpath = ""
        if getattr(sys, 'frozen', False):
            filedirpath = os.path.dirname(sys.executable)
        else:
            filedirpath = os.path.dirname(os.path.abspath(__file__))
            filedirpath = os.path.dirname(filedirpath)
        return filedirpath
    
    def get_cookies_path(self):
        return os.path.join(self.basedir, "cookies", "cookies.txt")

    def main(self):
        ffmpeg_path = None
        nodejs_path = None
        
        if self.check_ffmpeg():
            if platform.system().lower() == "windows":
                ffmpeg_path = "ffmpeg/bin/"
            else:
                ffmpeg_path = "ffmpeg/ffmpeg"
            pass
        else:
            ffmpeg_path = self.setffmpeg()
        if self.check_nodejs():
            if platform.system().lower() == "windows":
                nodejs_path = "node/"
            else:
                nodejs_path = "node/bin/node"
            pass
        else:
            nodejs_path = self.setnodejs()

        if not self.checkconfig():
            config_path = self.generate_config()
        else:
            config_path = os.path.join(self.basedir, "config", "config")

        self.create_cookies()
        self.checkcookies()
        if not self.checkcookies():
            print("please put cookies.txt file into cookies folder")

        with open(config_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        ffmpeginfo = f'--ffmpeg-location "{os.path.abspath(os.path.join(self.basedir, ffmpeg_path))}"' if ffmpeg_path else ""
        nodejsinfo = f'--js-runtimes node:"{os.path.abspath(os.path.join(self.basedir, nodejs_path))}"' if nodejs_path else ""
        cookiesinfo = f'--cookies "{os.path.abspath(os.path.join(self.basedir, self.get_cookies_path()))}"'
        lines = self.configupdate(lines, "# --exec [WHEN:]CMD", ffmpeginfo, "insert")
        lines = self.configupdate(lines, "# --remote-components COMPONENT", nodejsinfo, "insert")
        lines = self.configupdate(lines, '--cookies cookies/cookies.txt', cookiesinfo, "replace")

        # 写回文件
        with open(config_path, "w", encoding="utf-8") as f:
            f.writelines(lines)


if __name__ == "__main__":
    config_gen = ConfigGenerator()
    # config_gen.main()