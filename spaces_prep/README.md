Get the space URL and get the MP3 file using [Lychee](https://www.lychee.so/download-space)

Download the MP3 file and save it as `input.mp3`

Cut quiet beginning:

```bash
ffmpeg -i input.mp3 -ss 00:02:25 -acodec copy cut_beginning.mp3
```

Cut quiet ending:

```bash
ffmpeg -i cut_beginning.mp3 -to 01:32:44 -acodec copy cut_ending.mp3
```

Split into 30-minute parts:

```bash
python split_mp3.py cut_ending.mp3
```

Enhance all parts using [Adobe Podcast](https://podcast.adobe.com/enhance)

Stitch all parts together:

```bash
python stitch_mp3.py
```
