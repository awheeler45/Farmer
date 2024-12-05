# Farmer
The Farmer Was Replaced

## Changelog
12.4.24
- Added new item dictionary for maxItems. It will now farm items only if they fall below min and will stay on that item until it hits its max.
- Added checks for Power as well to ensure we always have power before farming other items.
- (Bug fix) Fixed an issue with sunflower() being called twice resulting in some bad flower picks. It will now only decrement as intended and no longer pick at the wrong time.
- Updated the sunflower function, its a little bit faster now.
- Added a changelog.

## Goals
- I want to make the planter function more robust, right now it feels to slow to me.
- Next up? Cacti! The next major update will include a function for the cactus plant, as well as a sorting routine.