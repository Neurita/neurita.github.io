#Credits

This theme is completly based on [Maurizio Sambati theme](https://github.com/duilio/pelican-octopress-theme), so the all
credit goes to him.

#Pelipress 

This is a theme for [Pelican](http://blog.getpelican.com/) that looks like [Octopress](http://octopress.org/) default theme but with some changes for my personal blog
<http://josejimenez.net>. 

##A screenshot
![Screenshot](http://gallifrey.es/images/pelipress_josejimenez.png)

##Plugins

This theme add a nice section on the sidebar with a list of GitHub repositories of the user.
You can enable it by using these settings:

- ``GITHUB_USER``: (required to enable) username
- ``GITHUB_REPO_COUNT``: 5
- ``GITHUB_SKIP_FORK``: False
- ``GITHUB_SHOW_USER_LINK``: False

##Configurations in this theme
The following settings are available to use:

- ``MENUBRAND``: Text and link for the brand of the blog. For example::

    ```python
    [('Jose Jiménez', 'http://josejimenez.net'),]
    ```

- ``SOCIAL_SIDEBAR_TOP``: List of social links showed at the top of the sidebar, see an example at http://josejimenez.net For example::
    
    ```python
    SOCIAL_SIDEBAR_TOP = (
          ('Google+', 'https://plus.google.com/116700712402100417502/posts', '<i class="icon-google-plus-sign"></i>'),
          ('Twitter', 'https://twitter.com/vrolloc', '<i class="icon-twitter-sign"></i>'),
          )
    ```

- ``HIDE_CATEGORIES_SIDEBAR``: If True, the categories won't be shown in the sidebar.
