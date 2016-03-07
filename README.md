sixdegreestravel
================

### A travel-oriented social network. Connect with friends and travel light!


6 Degrees is built on a neo4j graph database and a python back end. 


Installation
---
requirements:
 - Python
 	- pip
 	- virtualenv
 	- pip install -r requirements.txt

 - neo4j

 



## Directory structure

```
.
├── README.md
├── app
│   ├── __init__.py
│   ├── indexes.py
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   │   ├── ie.css
│   │   │   ├── ie.css.map
│   │   │   ├── styles.css
│   │   │   └── styles.css.map
│   │   ├── fonts
│   │   │   └── ...
│   │   ├── img
│   │   │   └── ...
│   │   ├── js
│   │   │   ├── global.js
│   │   │   ├── libs
│   │   │   │   └── modernizr.custom.js
│   │   │   └── plugins.js
│   │   └── scss
│   │       ├── _shame.scss 					# because hacks happen
│   │       ├── base 							# reset, typography, site-wide
│   │       │   ├── _base.scss 				# imports for all base styles
│   │       │   ├── _index.scss 				# base styles
│   │       │   ├── _layout.scss
│   │       │   └── _normalize.scss 			# normalize v3.0.1
│   │       ├── ie.scss
│   │       ├── layout 						# major components, e.g., header, footer etc.
│   │       │   └── _index.scss 				# imports for all layout styles
│   │       ├── lib
│   │       │   └──...
│   │       ├── modules 						# minor components, e.g., buttons, widgets etc.
│   │       │   ├── _buttons.scss 			# imports for all modules
│   │       │   └── _index.scss
│   │       ├── states 						# js-based classes, alternative states e.g., success or error state
│   │       │   ├── _index.scss 				# imports for all state styles
│   │       │   ├── _print.scss 				# print styles
│   │       │   ├── _states.scss 				# state rules
│   │       │   └── _touch.scss 				# touch styles
│   │       ├── styles.scss 					# primary Sass file
│   │       └── utilities 					# non-CSS outputs (i.e. mixins, variables) & non-modules				
│   │           ├── _fonts.scss 				# @font-face mixins
│   │           ├── _functions.scss 			# ems to rems conversion, etc.
│   │           ├── _global.scss 				# global variables
│   │           ├── _helpers.scss 			# placeholder helper classes
│   │           ├── _index.scss 				# imports for all mixins + global project variables
│   │           └── _mixins.scss 				# media queries, CSS3, etc.
│   ├── templates
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── logout.html
│   │   ├── map.html
│   │   ├── profile.html
│   │   └── register.html
│   └── views.py
├── requirements.txt
└── run.py

  
```