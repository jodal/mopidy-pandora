**************
Mopidy-Pandora
**************

.. image:: https://img.shields.io/pypi/v/Mopidy-Pandora
    :target: https://pypi.org/project/Mopidy-Pandora/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/circleci/build/gh/mopidy/mopidy-pandora
    :target: https://circleci.com/gh/mopidy/mopidy-pandora
    :alt: CircleCI build status

.. image:: https://img.shields.io/codecov/c/gh/mopidy/mopidy-pandora
    :target: https://codecov.io/gh/mopidy/mopidy-pandora
    :alt: Test coverage

`Mopidy <https://mopidy.com/>`_ extension for playing music from `Pandora <https://www.pandora.com/>`_.


Maintainer wanted
=================

I no longer have access to the Pandora music service in the region that I live, which has made maintaining this project
impossible. Mopidy-Pandora is looking for a new maintainer, preferably someone who is familiar with the codebase,
familiar with Python development, and uses the paid Pandora subscription service on a regular basis.

If you're interested, please take a look at the code base and work on submitting a pull request or two to show you
understand how everything works together.

Features
========

- Support for both Pandora Premium and ad-supported free accounts.
- Add ratings to tracks (thumbs up, thumbs down, sleep, etc.).
- Bookmark songs or artists.
- Browse and add genre stations.
- Search for song, artist, and genre stations.
- Play QuickMix stations.
- Sort stations alphabetically or by date added.
- Delete stations from the user's Pandora profile.
- Scrobbling to last.fm using the `Mopidy scrobbler <https://github.com/mopidy/mopidy-scrobbler>`_.


Usage
=====

Ideally, Mopidy needs `dynamic playlists <https://github.com/mopidy/mopidy/issues/620>`_ and
`core extensions <https://github.com/mopidy/mopidy/issues/1100>`_ to properly support Pandora. In the meantime,
Mopidy-Pandora comes bundled with a frontend extension that automatically adds more tracks to the tracklist as needed.
Mopidy-Pandora will ensure that there are always just two tracks in the tracklist: the currently playing track and the
track that is up next. It is not possible to mix Pandora and non-Pandora tracks for playback at the same time, so any
non-Pandora tracks will be removed from the tracklist when playback starts.

Pandora expects users to interact with tracks at the point in time and in the sequence that it serves them up. For this
reason, trying to save tracks to playlists or messing with the Mopidy-Pandora generated tracklist is probably not a good
idea. And not recommended.


Dependencies
============

- Requires a Pandora user account. Users with a Pandora Premium subscription will have access to the higher quality 192 Kbps
  audio stream. Free accounts will play advertisements.

- ``pydora`` >= 2,<3. The Python Pandora API Client. **Pre-requisites**: As of 1.11.0 pydora requires `cryptography <https://pypi.python.org/pypi/cryptography>`_.
  Depending on your setup, there may be some native dependencies on openssl that you will need to install beforehand.
  See the `cryptography installation docs <https://cryptography.io/en/latest/installation/>`_ for details.

- ``cachetools`` >= 1.0.0. Extensible memoizing collections and decorators. The package is available as ``cachetools``
  on PyPI.

- ``Mopidy`` >= 3.0.0. The music server that Mopidy-Pandora extends.

- ``requests`` >= 2.5.0. Python HTTP Requests for Humans™.


Installation
============

Install by running::

    pip install Mopidy-Pandora


Configuration
=============

Before starting Mopidy, you must add your Pandora username and password to your Mopidy configuration file. The minimum
configuration also requires that you provide the details of the JSON API endpoint that you would like to use::

    [pandora]
    enabled = true
    api_host = tuner.pandora.com/services/json/
    partner_encryption_key =
    partner_decryption_key =
    partner_username = android
    partner_password =
    partner_device = android-generic
    username =
    password =

The following configuration values are available:

- ``pandora/enabled``: If the Pandora extension should be enabled or not. Defaults to ``true``.

- ``pandora/api_host``: Which of the JSON API `endpoints <https://6xq.net/pandora-apidoc/json/>`_ to use. Note that
  the endpoints are different for Pandora Premium and free accounts (details in the link provided).

- ``pandora/partner_*`` related values: The `credentials <https://6xq.net/playground/pandora-apidoc/json/partners/#partners>`_
  to use for the Pandora API entry point. You *must* provide these values based on your device preferences.

- ``pandora/username``: Your Pandora username. You *must* provide this.

- ``pandora/password``: Your Pandora password. You *must* provide this.

- ``pandora/preferred_audio_quality``: can be one of ``lowQuality``, ``mediumQuality``, or ``highQuality`` (default).
  If the preferred audio quality is not available for the partner device specified, then the next-lowest bitrate stream
  that Pandora supports for the chosen device will be used. Note that this setting has no effect for partner device types
  that only provide one audio stream (notably credentials associated with iOS). In such instances, Mopidy-Pandora will
  always revert to the default stream provided by the Pandora server.

- ``pandora/sort_order``: defaults to ``a-z``. Use ``date`` to display the list of stations in the order that the
  stations were added.

- ``pandora/auto_setup``: Specifies if Mopidy-Pandora should automatically configure the Mopidy player for best
  compatibility with the Pandora radio stream. Defaults to ``true`` and turns ``consume`` on and ``repeat``, ``random``,
  and ``single`` modes off.

- ``pandora/cache_time_to_live``: specifies the length of time (in seconds) that station and genre lists should be cached
  for between automatic refreshes. Using a local cache greatly speeds up browsing the library. It should not be necessary
  to fiddle with this unless the Mopidy frontend that you are using does not support manually refreshing the library,
  and you want Mopidy-Pandora to immediately detect changes to your Pandora user profile that are made in other Pandora
  players. Setting this to ``0`` will disable caching completely and ensure that the latest lists are always retrieved
  directly from the Pandora server. Defaults to ``86400`` (i.e. 24 hours).

It is also possible to apply Pandora ratings and perform other actions on the currently playing track using the standard
pause/play/previous/next buttons.

- ``pandora/event_support_enabled``: setting this to ``true`` will enable the event triggers. Event support is disabled
  by default as this is still an experimental feature, and not something that is provided for in the Mopidy API. It works,
  but it is not impossible that the wrong events may be triggered for tracks or (in the worst case scenario) that one of
  your stations may be deleted accidentally. Mileage may vary - **use at your own risk.**
- ``pandora/double_click_interval``: successive button clicks that occur within this interval will trigger an event.
  Defaults to ``2.50`` seconds.
- ``pandora/on_pause_resume_click``: click pause and then play while a song is playing to trigger the event. Defaults
  to ``thumbs_up``.
- ``pandora/on_pause_next_click``: click pause and then next in quick succession. Calls event and skips to next song.
  Defaults to ``thumbs_down``.
- ``pandora/on_pause_previous_click``: click pause and then previous in quick succession. Calls event and restarts the
  current song. Defaults to ``sleep``.
- ``pandora/on_pause_resume_pause_click``: click pause, resume, and pause again in quick succession (i.e. triple click).
  Calls event. Defaults to ``delete_station``.

The full list of supported events are: ``thumbs_up``, ``thumbs_down``, ``sleep``, ``add_artist_bookmark``,
``add_song_bookmark``, and ``delete_station``.


Project resources
=================

- `Source code <https://github.com/mopidy/mopidy-pandora>`_
- `Issue tracker <https://github.com/mopidy/mopidy-pandora/issues>`_
- `Changelog <https://github.com/mopidy/mopidy-pandora/releases>`_
- `Troubleshooting guide <https://github.com/mopidy/mopidy-pandora/blob/master/docs/troubleshooting.rst>`_

Credits
=======

- Original author: `Andrew Wason <https://github.com/rectalogic>`__
- Current maintainer: `John Cass <https://github.com/jcass77>`__
- `Contributors <https://github.com/mopidy/mopidy-pandora/graphs/contributors>`_
