library(RefManageR)
library(dplyr)

removeBold <- function(aut.l){
  aut.l$given = grep('\\\\bf', aut.l$given, value=TRUE, invert=TRUE)
  aut.l$family = grep('\\\\bf', aut.l$family, value=TRUE, invert=TRUE)
  return(aut.l)
}
convertStars <- function(cc){
  cc %>% gsub('\\*', '\\\\*', .)
}

bib <- ReadBib('JM-publication.bib')

bibi = bib[[1]]

for(bibi in bib){
  auths = lapply(bibi$author, function(aul){
    aul = removeBold(aul)
    paste(aul$family, aul$given)
  }) %>% unlist
  auths = paste(auths, collapse=', ')
  title = bibi$title %>% gsub('\\{','',.) %>% gsub('\\}','',.) %>%
    gsub('\n','',.) %>% gsub(' +',' ',.)
  journal = gsub(".*\\{.*\\}\\{(.+)\\}", "\\1", bibi$journal)
  year = bibi$year
  doi = paste0('DOI:', bibi$doi)
  cat(paste0(c(auths, title, journal, year, doi), collapse='. '), '\n\n')
}

