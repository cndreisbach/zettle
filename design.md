# Zettlekasten software

* Very accessible interface
* Main page is search or add a note
  * When searching, search live-updates, showing note previews
* One key/click to create a new note
  * One key-press (+) to bring up add note interface
  * One key-press (Esc) to get out of add note interface
* Every note has a very short slug (1CD9) 
* When editing notes, linking to other notes is as easy as possible. Search by title/contents/short slug

## Models

* Note
  * title (optional)
  * text (max length ~1000 characters)
  * shortcode (autogenerated)
  * links to other notes (has and belongs to many)
  * tags (has and belongs to many)

## Visual Design

- Textmark (https://fonts.google.com/specimen/Fredoka+One)
- Main font - Roboto or Plex (https://fonts.google.com/featured/Plex)


## JavaScript

- Try intercooler
