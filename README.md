This repo contains the content of my personal page hosted at https://jmonlong.github.io/.
It's a [blogdown](https://bookdown.org/yihui/blogdown/) website so it can be built using:

```R
library(blogdown)
serve_site()
stop_server()
build_site(build_rmd=TRUE)
```

Note: for some reasons, it only works by running these commands interactively in R. I get an error when trying to use `Rscript`, although maybe it still works.

I write my CV in latex, see the [misc](misc) folder which contains the BibTeX library with my publications and the LaTeX document and style.
Note: the BibTeX file is also used for the ["Selected  Publications" section](content/home/publications.Rmd) of the website (using the [RefManageR package](https://cran.r-project.org/web/packages/RefManageR/index.html))


## Misc changes

### Minimal/isolated pages

I've added a parameter to enable a "minimal" mode for *fixed* pages.
The page has no navigation bar at the top, or links to other pages at the bottom. 
It can be useful when I want just an isolated random page on the internet somewehere.

To add a page, write a `.md` markdown page in `content/fixed/` and include `minimal = true` in the header.

### Include images

1. Stored in `static/img`.
2. Used in pages with `![](/img/myimg.jpg)`

To resize an image to be half the page width, add *half* as alt text: `![half](/img/myimg.jpg)`
This was defined in the CSS file at `themes/hugo-academic/static/css/hugo-academic.css`.

