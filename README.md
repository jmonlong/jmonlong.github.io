This repo contains the content of my personal page (https://github.com/jmonlong/jmonlong.github.io) hosted at https://jmonlong.github.io/.
As far as I remember, either at the time or still now, the static files had to be in the root folder of https://github.com/jmonlong/jmonlong.github.io.
A way to use blogdown was then to setup another repo (this one) with the content and compile it in a `public` folder that is actually a sub-module linking to https://github.com/jmonlong/jmonlong.github.io.

To setup the `public` folder I ran: `git submodule add -b master git@github.com:jmonlong/jmonlong.github.io.git public`

Then, when I want to update the content, I do:

```
make pull
## update the content
make serve
MSG="a commit message" make deploy
```

Note: It looks like this 2-repo setup is not necessary anymore. 
I'll try to switch to a simpler 1-repo system soon.
