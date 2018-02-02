# Render HTML to PDF with page breaks

This repo was produced as an answer to [this question](https://stackoverflow.com/questions/48581654/writing-multiple-page-pdf-from-html-template-using-weasy-print-and-django) on stack overflow.

## Installation

```shell
git clone git@github.com:Asday/weasyprint-pagination.git
cd weasyprint-pagination
mkvirtualenv --python=$(which python3.6) weasyprint-pagination
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000
```

Then visit [/](http://127.0.0.1:8000/).

For an HTML preview, check out [/?html](http://127.0.0.1:8000/).
