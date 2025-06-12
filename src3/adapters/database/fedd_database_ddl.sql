create table if not exists feed.albums
(
    id_album            int auto_increment
        primary key,
    upc_album           varchar(20)                         null,
    name_album          text                                null,
    subtitle_album      varchar(200)                        null,
    release_type_album  varchar(25)                         null,
    length_album        time                                null,
    tracks_qty_album    int                                 null,
    release_date_album  datetime                            null,
    active_album        tinyint                             null,
    specific_data_album json                                null,
    audi_edited_album   timestamp                           null,
    audi_created_album  timestamp default CURRENT_TIMESTAMP not null,
    update_id_message   int       default 0                 not null,
    insert_id_message   int       default 0                 not null
);

create index albums_audi_created_album_IDX
    on feed.albums (audi_created_album);

create index albums_audi_edited_album_IDX
    on feed.albums (audi_edited_album);

create index albums_insert_id_message_IDX
    on feed.albums (insert_id_message);

create index albums_upc_album_IDX
    on feed.albums (upc_album);

create index albums_update_id_message_IDX
    on feed.albums (update_id_message);

create table if not exists feed.albums_artists
(
    id_album_artist                   int auto_increment
        primary key,
    id_album                          int                                 null,
    id_artist                         int                                 null,
    artist_role_album_artist          varchar(100)                        null,
    active_album_artist               tinyint   default 1                 not null,
    manually_edited_album_artist      tinyint   default 0                 not null,
    audi_manually_edited_album_artist timestamp                           null,
    audi_edited_album_artist          timestamp                           null,
    audi_created_album_artist         timestamp default CURRENT_TIMESTAMP not null,
    update_id_message                 int       default 0                 not null,
    insert_id_message                 int       default 0                 not null,
    constraint albums_artists_UN
        unique (id_album, id_artist, artist_role_album_artist)
);

create index albums_artists_audi_created_album_artist_IDX
    on feed.albums_artists (audi_created_album_artist);

create index albums_artists_audi_edited_album_artist_IDX
    on feed.albums_artists (audi_edited_album_artist);

create index albums_artists_id_album_IDX
    on feed.albums_artists (id_album);

create index albums_artists_id_artist_IDX
    on feed.albums_artists (id_artist);

create index albums_artists_insert_id_message_IDX
    on feed.albums_artists (insert_id_message);

create index albums_artists_update_id_message_IDX
    on feed.albums_artists (update_id_message);

create table if not exists feed.albums_genres
(
    id_album_genre           int auto_increment
        primary key,
    id_album                 int                                 null,
    id_genre                 int                                 null,
    audi_edited_album_genre  timestamp                           null,
    audi_created_album_genre timestamp default CURRENT_TIMESTAMP not null,
    update_id_message        int       default 0                 not null,
    insert_id_message        int       default 0                 not null,
    constraint albums_genres_UN
        unique (id_album, id_genre)
);

create index albums_genres_audi_created_album_genre_IDX
    on feed.albums_genres (audi_created_album_genre);

create index albums_genres_audi_edited_album_genre_IDX
    on feed.albums_genres (audi_edited_album_genre);

create index albums_genres_id_album_IDX
    on feed.albums_genres (id_album);

create index albums_genres_id_genre_IDX
    on feed.albums_genres (id_genre);

create index albums_genres_insert_id_message_IDX
    on feed.albums_genres (insert_id_message);

create index albums_genres_update_id_message_IDX
    on feed.albums_genres (update_id_message);

create table if not exists feed.albums_rights
(
    id_albright           bigint auto_increment
        primary key,
    id_album              bigint                              null,
    id_dist               int                                 null,
    id_label              int                                 null,
    id_cmt                int                                 null,
    id_use_type           int                                 null,
    cnty_ids_albright     json                                null,
    start_date_albright   datetime                            null,
    end_date_albright     datetime                            null,
    audi_edited_albright  timestamp                           null,
    audi_created_albright timestamp default CURRENT_TIMESTAMP not null,
    update_id_message     int       default 0                 not null,
    insert_id_message     int       default 0                 not null,
    constraint albums_rights_UN
        unique (id_album, id_dist, id_label, id_cmt, id_use_type)
);

create index albums_rights_audi_created_albright_IDX
    on feed.albums_rights (audi_created_albright);

create index albums_rights_audi_edited_albright_IDX
    on feed.albums_rights (audi_edited_albright);

create index albums_rights_id_album_distributor_IDX
    on feed.albums_rights (id_album, id_dist);

create index albums_rights_id_album_label_IDX
    on feed.albums_rights (id_album, id_label);

create index albums_rights_insert_id_message_IDX
    on feed.albums_rights (insert_id_message);

create index albums_rights_update_id_message_IDX
    on feed.albums_rights (update_id_message);

create table if not exists feed.albums_tracks
(
    id_album_track           int auto_increment
        primary key,
    id_album                 int                                 null,
    id_track                 int                                 null,
    volume_album_track       int                                 null,
    number_album_track       int                                 null,
    audi_edited_album_track  timestamp                           null,
    audi_created_album_track timestamp default CURRENT_TIMESTAMP not null,
    update_id_message        int       default 0                 not null,
    insert_id_message        int       default 0                 not null,
    constraint albums_tracks_UN
        unique (id_album, id_track)
);

create index albums_tracks_audi_created_album_track_IDX
    on feed.albums_tracks (audi_created_album_track);

create index albums_tracks_audi_edited_album_track_IDX
    on feed.albums_tracks (audi_edited_album_track);

create index albums_tracks_id_album_IDX
    on feed.albums_tracks (id_album);

create index albums_tracks_id_track_IDX
    on feed.albums_tracks (id_track);

create index albums_tracks_insert_id_message_IDX
    on feed.albums_tracks (insert_id_message);

create index albums_tracks_update_id_message_IDX
    on feed.albums_tracks (update_id_message);

create table if not exists feed.albums_tracks_rights
(
    id_albtraright           bigint auto_increment
        primary key,
    id_album_track           bigint                              null,
    id_dist                  int                                 null,
    id_label                 int                                 null,
    id_cmt                   int                                 null,
    id_use_type              int                                 null,
    cnty_ids_albtraright     json                                null,
    start_date_albtraright   datetime                            null,
    end_date_albtraright     datetime                            null,
    pline_text_albtraright   text                                null,
    pline_year_albtraright   text                                null,
    audi_edited_albtraright  timestamp                           null,
    audi_created_albtraright timestamp default CURRENT_TIMESTAMP not null,
    update_id_message        int       default 0                 not null,
    insert_id_message        int       default 0                 not null,
    constraint albums_tracks_rights_UN
        unique (id_album_track, id_dist, id_label, id_cmt, id_use_type)
);

create index albums_tracks_rights_id_album_track_IDX
    on feed.albums_tracks_rights (id_album_track);

create index albums_tracks_rights_id_album_track_id_dist_IDX
    on feed.albums_tracks_rights (id_album_track, id_dist);

create index albums_tracks_rights_id_album_track_id_label_IDX
    on feed.albums_tracks_rights (id_album_track, id_label);

create table if not exists feed.artists
(
    id_artist            int auto_increment
        primary key,
    name_artist          mediumtext                          null,
    id_parent_artist     int                                 null,
    active_artist        tinyint                             null,
    specific_data_artist json                                null,
    audi_edited_artist   timestamp                           null,
    audi_created_artist  timestamp default CURRENT_TIMESTAMP not null,
    update_id_message    int       default 0                 not null,
    insert_id_message    int       default 0                 not null
);

create index artists_audi_created_artist_IDX
    on feed.artists (audi_created_artist);

create index artists_audi_edited_artist_IDX
    on feed.artists (audi_edited_artist);

create index artists_id_parent_artist_IDX
    on feed.artists (id_parent_artist);

create index artists_insert_id_message_IDX
    on feed.artists (insert_id_message);

create index artists_name_artist_IDX
    on feed.artists (name_artist(255));

create index artists_update_id_message_IDX
    on feed.artists (update_id_message);

create fulltext index name_artist
    on feed.artists (name_artist);

create table if not exists feed.comercial_model_types
(
    id_cmt            int auto_increment
        primary key,
    name_cmt          text                                null,
    description_cmt   text                                null,
    audi_edited_cmt   timestamp                           null,
    audi_created_cmt  timestamp default CURRENT_TIMESTAMP not null,
    update_id_message int       default 0                 not null,
    insert_id_message int       default 0                 not null,
    constraint cmt_name_use_type
        unique (name_cmt(100))
);

create index comercial_model_types_name_cmt_IDX
    on feed.comercial_model_types (name_cmt(100));

create table if not exists feed.contributors
(
    id_contri           int auto_increment
        primary key,
    name_contri         text                                null,
    active_contri       tinyint                             null,
    audi_edited_contri  timestamp                           null,
    audi_created_contri timestamp default CURRENT_TIMESTAMP not null,
    update_id_message   int       default 0                 not null,
    insert_id_message   int       default 0                 not null,
    constraint constr_contributors
        unique (name_contri(100))
);

create index contributors_audi_created_contri_IDX
    on feed.contributors (audi_created_contri);

create index contributors_audi_edited_contri_IDX
    on feed.contributors (audi_edited_contri);

create index contributors_insert_id_message_IDX
    on feed.contributors (insert_id_message);

create index contributors_name_contri_IDX
    on feed.contributors (name_contri(50));

create index contributors_update_id_message_IDX
    on feed.contributors (update_id_message);

create table if not exists feed.erns
(
    id_ern                            int auto_increment
        primary key,
    sqs_message_id_ern                varchar(255)                      null,
    sqs_receipt_handle_ern            text                              null,
    sqs_md5_of_body_ern               varchar(255)                      null,
    origin_ern                        varchar(255)                      null,
    bucket_ern                        varchar(255)                      null,
    key_path_ern                      text                              null,
    delivery_timestamp_ern            datetime                          null,
    sqs_insert_timestamp_ern          datetime                          null,
    batch_id_ern                      varchar(255)                      null,
    batch_timestamp_ern               datetime                          null,
    upc_identifier_ern                varchar(255)                      null,
    status_processed_resources_ern    varchar(255) default 'PENDING'    not null,
    sent_to_process_resources_qty_ern int          default 0            not null,
    processed_resources_qty_ern       int          default 0            not null,
    status_loaded_to_catalog_ern      varchar(255) default 'PROCESSING' not null,
    status_resources_copied_to_s3_ern varchar(255) default 'PENDING'    not null,
    status_activated_message_ern      varchar(255) default 'PENDING'    not null,
    status_ack_sent_ern               varchar(255) default 'PENDING'    not null
);

create index s3_delivery_data_message_id_IDX
    on feed.erns (sqs_message_id_ern);

create table if not exists feed.genres
(
    id_genre           int auto_increment
        primary key,
    name_genre         varchar(100)                        null,
    active_genre       tinyint                             null,
    audi_edited_genre  timestamp                           null,
    audi_created_genre timestamp default CURRENT_TIMESTAMP not null,
    update_id_message  int       default 0                 not null,
    insert_id_message  int       default 0                 not null,
    constraint genres_unique
        unique (name_genre)
);

create index genres_name_genre_IDX
    on feed.genres (name_genre);

create table if not exists feed.labels
(
    id_label           int auto_increment
        primary key,
    name_label         varchar(50)                         null,
    active_label       tinyint                             null,
    audi_edited_label  timestamp                           null,
    audi_created_label timestamp default CURRENT_TIMESTAMP not null,
    update_id_message  int       default 0                 not null,
    insert_id_message  int       default 0                 not null,
    constraint labels_unique
        unique (name_label)
);

create index labels_name_label_IDX
    on feed.labels (name_label);

create table if not exists feed.orch_parameters
(
    param_id                int auto_increment
        primary key,
    param_code              int        null,
    param_name              text       null,
    param_long_name         text       null,
    param_numeric_value     decimal    null,
    param_boolean_value     tinyint(1) null,
    param_string_value      text       null,
    param_deactivation_date timestamp  null,
    param_activation_date   timestamp  null,
    param_order             int        null,
    param_description       text       null,
    param_substitute_code   int        null
);

create table if not exists feed.resources
(
    id_reso                                             bigint auto_increment
        primary key,
    id_ern                                              bigint                                 not null,
    reference_reso                                      text                                   null,
    isrc_reso                                           text                                   null,
    technical_detail_reference_reso                     text                                   null,
    type_reso                                           text                                   not null,
    is_preview_reso                                     text                                   null,
    is_url_reso                                         int          default 0                 not null,
    file_path_reso                                      longtext                               null,
    file_url_reso                                       text                                   null,
    audio_codec_type_reso                               text                                   null,
    image_codec_type_reso                               text                                   null,
    bit_rate_reso                                       text                                   null,
    number_of_channels_reso                             text                                   null,
    sampling_rate_reso                                  text                                   null,
    bits_per_sample_reso                                text                                   null,
    preview_start_point_reso                            int                                    null,
    preview_end_point_reso                              int                                    null,
    preview_duration_reso                               time                                   null,
    file_hash_sum_reso                                  text                                   null,
    file_hash_sum_algorithm_type_reso                   text                                   null,
    status_processed_128_reso                           varchar(100)                           null,
    status_processed_result_128_message_reso            text                                   null,
    status_processed_320_reso                           varchar(100)                           null,
    status_processed_result_320_message_reso            text                                   null,
    status_processed_custom_preview_reso                varchar(100)                           null,
    status_processed_result_custom_preview_message_reso text                                   null,
    status_processed_image_reso                         varchar(100)                           null,
    status_processed_result_image_message_reso          text                                   null,
    status_copied_to_catalog_128_reso                   varchar(100) default 'PENDING'         not null,
    status_copied_to_catalog_320_reso                   varchar(100) default 'PENDING'         not null,
    status_copied_to_catalog_image_reso                 varchar(100) default 'PENDING'         not null,
    audi_edited_reso                                    timestamp                              null,
    audi_created_reso                                   timestamp    default CURRENT_TIMESTAMP not null
);

create index resources_audi_edited_reso_IDX
    on feed.resources (audi_edited_reso);

create index resources_id_ern_IDX
    on feed.resources (id_ern, reference_reso(10), technical_detail_reference_reso(10));

create index resources_id_resource_IDX
    on feed.resources (id_reso);

create table if not exists feed.s3_delivery_data
(
    id                            int auto_increment
        primary key,
    message_id                    varchar(255)                      null,
    receipt_handle                text                              null,
    md5_of_body                   varchar(255)                      null,
    origin                        varchar(255)                      null,
    bucket                        varchar(255)                      null,
    key_path                      text                              null,
    delivery_timestamp            datetime                          null,
    sqs_insert_timestamp          datetime                          null,
    batch_id                      varchar(255)                      null,
    batch_timestamp               datetime                          null,
    upc_or_grid                   varchar(255)                      null,
    status_processed_resources    varchar(255) default 'PENDING'    not null,
    sent_to_process_resources_qty int          default 0            not null,
    processed_resources_qty       int          default 0            not null,
    status_loaded_to_catalog      varchar(255) default 'PROCESSING' not null,
    status_resources_copied_to_s3 varchar(255) default 'PENDING'    not null,
    status_activated_message      varchar(255) default 'PENDING'    not null,
    status_ack_sent               varchar(255) default 'PENDING'    not null
);

create index s3_delivery_data_message_id_IDX
    on feed.s3_delivery_data (message_id);

create table if not exists feed.tracks
(
    id_track            int auto_increment
        primary key,
    isrc_track          varchar(20)                         null,
    name_track          text                                null,
    version_track       text                                null,
    length_track        time                                null,
    explicit_track      tinyint                             null,
    active_track        tinyint                             null,
    specific_data_track json                                null,
    audi_edited_track   timestamp                           null,
    audi_created_track  timestamp default CURRENT_TIMESTAMP not null,
    update_id_message   int       default 0                 not null,
    insert_id_message   int       default 0                 not null,
    constraint constr_isrc_track
        unique (isrc_track)
);

create index tracks_audi_created_track_IDX
    on feed.tracks (audi_created_track);

create index tracks_audi_edited_track_IDX
    on feed.tracks (audi_edited_track);

create index tracks_insert_id_message_IDX
    on feed.tracks (insert_id_message);

create index tracks_isrc_track_IDX
    on feed.tracks (isrc_track);

create index tracks_update_id_message_IDX
    on feed.tracks (update_id_message);

create table if not exists feed.tracks_artists
(
    id_track_artist                   int auto_increment
        primary key,
    id_track                          int                                 null,
    id_artist                         int                                 null,
    artist_role_track_artist          varchar(100)                        null,
    audi_edited_track_artist          timestamp                           null,
    audi_created_track_artist         timestamp default CURRENT_TIMESTAMP not null,
    update_id_message                 int       default 0                 not null,
    insert_id_message                 int       default 0                 not null,
    active_track_artist               tinyint   default 1                 not null,
    manually_edited_track_artist      tinyint   default 0                 not null,
    audi_manually_edited_track_artist timestamp                           null,
    constraint tracks_artists_UN
        unique (id_track, id_artist, artist_role_track_artist)
);

create index AK
    on feed.tracks_artists (id_track, id_artist);

create index tracks_artists_audi_created_track_artist_IDX
    on feed.tracks_artists (audi_created_track_artist);

create index tracks_artists_audi_edited_track_artist_IDX
    on feed.tracks_artists (audi_edited_track_artist);

create index tracks_artists_id_artist_IDX
    on feed.tracks_artists (id_artist);

create index tracks_artists_id_track_IDX
    on feed.tracks_artists (id_track);

create index tracks_artists_insert_id_message_IDX
    on feed.tracks_artists (insert_id_message);

create index tracks_artists_update_id_message_IDX
    on feed.tracks_artists (update_id_message);

create table if not exists feed.tracks_contributors
(
    id_track_contri                    int auto_increment
        primary key,
    id_track                           int                                 null,
    id_contri                          int                                 null,
    contributor_role_track_contri      text                                null,
    contributor_role_type_track_contri text                                null,
    audi_edited_track_contri           timestamp                           null,
    audi_created_track_contri          timestamp default CURRENT_TIMESTAMP not null,
    update_id_message                  int       default 0                 not null,
    insert_id_message                  int       default 0                 not null,
    constraint tracks_contributors_UN
        unique (id_track, id_contri, contributor_role_track_contri(200), contributor_role_type_track_contri(200))
);

create index tracks_contributors_audi_created_track_contri_IDX
    on feed.tracks_contributors (audi_created_track_contri);

create index tracks_contributors_audi_edited_track_contri_IDX
    on feed.tracks_contributors (audi_edited_track_contri);

create index tracks_contributors_id_contri_IDX
    on feed.tracks_contributors (id_contri);

create index tracks_contributors_id_track_IDX
    on feed.tracks_contributors (id_track);

create index tracks_contributors_id_track_id_contry_IDX
    on feed.tracks_contributors (id_track, id_contri);

create index tracks_contributors_insert_id_message_IDX
    on feed.tracks_contributors (insert_id_message);

create index tracks_contributors_update_id_message_IDX
    on feed.tracks_contributors (update_id_message);

create table if not exists feed.use_types
(
    id_use_type           int auto_increment
        primary key,
    name_use_type         text                                null,
    description_use_type  text                                null,
    audi_edited_use_type  timestamp                           null,
    audi_created_use_type timestamp default CURRENT_TIMESTAMP not null,
    update_id_message     int       default 0                 null,
    insert_id_message     int       default 0                 null,
    constraint constr_name_use_type
        unique (name_use_type(100))
);

create index use_types_name_use_type_IDX
    on feed.use_types (name_use_type(100));

