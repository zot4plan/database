INSERT INTO playlists
(
	playlist_id, 
	thumbnail, 
	name, 
	shared_by, 
	original_url, 
	embed_url, 
	language, 
	is_verified
) 
VALUES
	(
        'PLSbcvcMOgs9EvNjev3R4LhcmubNH4Redk',
	    'FN7ALfpGxiI', 
	    'Simple Love (Vietnamese)', 
	    'LK', 
	    'https://youtube.com/playlist?list=PLSbcvcMOgs9EvNjev3R4LhcmubNH4Redk',
	    'https://www.youtube.com/embed/videoseries?list=PLSbcvcMOgs9EvNjev3R4LhcmubNH4Redk',
	    'Vietnamese',
        True
    ),
    (
        'PLSbcvcMOgs9E-8paOqVvdkDiBa4jeag1Y',
	    'nSpYpZEcv8U',
	    'Aloha (Korean)',
	    'LK',
	    'https://youtube.com/playlist?list=PLSbcvcMOgs9E-8paOqVvdkDiBa4jeag1Y',
	    'https://www.youtube.com/embed/videoseries?list=PLSbcvcMOgs9E-8paOqVvdkDiBa4jeag1Y',
	    'Korean',
        True
    ),
	(
		'PLSbcvcMOgs9EFd-Vk_mjCvHiYKTcjG99o',
	    'XLMu3CEwlcI',
	    'Suteki Da Ne (Japanese)',
	    'LK',
	    'https://youtube.com/playlist?list=PLSbcvcMOgs9EFd-Vk_mjCvHiYKTcjG99o',
	    'https://www.youtube.com/embed/videoseries?list=PLSbcvcMOgs9EFd-Vk_mjCvHiYKTcjG99o',
	    'Korean',
        True
	)
ON CONFLICT (playlist_id)
DO UPDATE SET
	thumbnail = EXCLUDED.thumbnail,
    name = EXCLUDED.name,
    author = EXCLUDED.author,
    shared_by = EXCLUDED.shared_by,
    original_url = EXCLUDED.original_url,
    embed_url = EXCLUDED.embed_url,
    language = EXCLUDED.language,
    genre = EXCLUDED.genre,
    is_verified = EXCLUDED.is_verified;