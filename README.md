# Videodigest: Automatic Video Summaries

Videodigest is a command-line utility for generating summaries of
videos by (1) applying an [automatic summarization](https://en.wikipedia.org/wiki/Automatic_summarization)
algorithm to their subtitles to find the N most important sentences,
then (2) compiling the video regions where those sentences appear.

Please cite this library if you end up using it academically:

APA style:

```Germanidis, A. (2015). Videodigest [Software]. Available from https://github.com/agermanidis/videodigest.```

Chicago style:

```Germanidis, A. 2015. Videodigest.```


### Installation

```
pip install videodigest
```

### Examples

* [The Empire Strikes Back](https://www.youtube.com/watch?v=IFbB3zXBnv4&index=4&list=PLdMqYckobjk4RMRMw7jR2xDfisWUvLSg1)
* [Clockwork Orange](https://www.youtube.com/watch?v=A5xVDWUnvuY)
* [Mr. Robot S01E10](https://www.youtube.com/watch?v=Q5dm3Zr72y8)

### Usage

```
$ videodigest -h
usage: videodigest: Automatic Video Summaries [-h] -i VIDEO_FILE -s
                                              SUBTITLES_FILE [-t DURATION]
                                              [-L LANGUAGE] [-S SUMMARIZER]
                                              [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -i VIDEO_FILE, --video-file VIDEO_FILE
                        Input video file
  -s SUBTITLES_FILE, --subtitles-file SUBTITLES_FILE
                        Input subtitle file (srt)
  -t DURATION, --duration DURATION
                        Duration of summary
  -L LANGUAGE, --language LANGUAGE
                        Language of subtitles
  -S SUMMARIZER, --summarizer SUMMARIZER
                        Auto-summarization algorithm (text-rank | luhn |
                        edmundson | lex-rank | lsa)
  -o OUTPUT, --output OUTPUT
                        Output file
```

### License

MIT
