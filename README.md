# Hub

The official Espanso's package repository

See [the website](https://hub.espanso.org/), and the docs containing [additional information on Packages](https://espanso.org/docs/packages/basics/)

## Review (Contributing new/update packages)

To review packages and merge policies, we met in Discord in our monthly meeting and talked about the subject. This is what we agreed that would be a in-between solution.

To be clear about the implications of using scripts in packages. We need to double check malicious or misinterpreted packages, so they don't cause damage (at least not permanent) in the point of reviewing PR. For example, nobody would want to have a trigger `a` that launches a command `rm -rf /`. So, in order to prevent it from happening:

- we have a CI that does some easy ground checks
- we double check every PR with a maintainer, just to be sure no mistakes are made
- we don't merge anything we don't understand
- we possibly reject packages that cause permanent damage to the system to prevent users of that packages to mistakenly cause trouble on their pcs.
- depending in a case by case scenario, we might allow to accept removing files in certain folders, for example `/tmp/`
- even if the package does not contain scripts, it needs a human reviewer nonetheless: it might have content that we don't want to be part of distributing, such as offensive/hateful language or images

The process of creating this review policy can be tracked in [#98](https://github.com/espanso/hub/issues/98)

## Run the package validation locally

Sometimes it's useful to run the validation process locally. To do so, you have
to make the following steps:

- have python 3.12 installed and make an environment in your local folder. We
use [`uv`](https://github.com/astral-sh/uv) often, and if you don't know it yet
, you should!

```bash
uv venv --python 3.12
```

- install the `pyyaml` dependency

```bash
uv pip install pyyaml
```

- run the `main.py` *from the root folder* (because the script uses `glob` to
find what packages are in the `packages/` folder)

```bash
uv run .github/scripts/validate/main.py
```

- wait until you have the results!

