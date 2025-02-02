# MkDocs Img2Fig v3 Plugin

> A simple regex is not going to cut it. Extends [MkDocs Img2Fig plugin](https://github.com/stuebersystems/mkdocs-img2fig-plugin)

This [MkDocs](https://www.mkdocs.org) plugin converts markdown encoded images like

```markdown
![An image caption](../images/my-image.png){align="right" width="20%"}
```

into 

```html
<figure class="figure-image">
  <img src="../../images/my-image.png" alt="An image caption" align="left" width="20%" >
  <figcaption>An image caption</figcaption>
</figure>
```

- of course, you could leave out `{align="right" width="20%"}`
- supported attr : https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/img

## Requirements

This package requires Python >=3.6 and MkDocs version 1.0 or higher.  

## Installation

Install the package with pip:

```cmd
pip install mkdocs-img2figv3-plugin @ git+https://github.com/AnotherGroupChat/mkdocs-img2figv3-plugin
# TODO: pip install mkdocs-img2figv3-plugin
```

Enable the plugin in your `mkdocs.yml`:

```yaml
plugins:
    - search
    - img2figv3
```

**Note:** If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set, but now you have to enable it explicitly.

More information about plugins in the [MkDocs documentation](https://www.mkdocs.org/user-guide/plugins/)

## Known issue

it won't work with setting `use_directory_urls: false` in your `mkdocs.yml` ( true is default )
