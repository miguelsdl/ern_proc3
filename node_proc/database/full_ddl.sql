-- Con los crete table (modelos) que te voy a pasar quiero
-- armar una clase que contenga todos los datos de un album,
-- sus artistas y tracks por ejemplo:

    Album {
        id_album: int,
        upc_album: string,
            Track {
                id_track: int,
                isrc_track: string,
                name_track: string unique,
        tracks: [
            Track {
                id_track: int,
                isrc_track: string,
                name_track: string unique,
            }
        ],
    }



-- Tabla albums
CREATE TABLE feed.albums (
    id_album            int auto_increment primary key,
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

-- Tabla albums_artists
CREATE TABLE feed.albums_artists (
    id_album_artist                   int auto_increment primary key,
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
    constraint albums_artists_UN unique (id_album, id_artist, artist_role_album_artist)
);

-- Tabla albums_genres
CREATE TABLE feed.albums_genres (
    id_album_genre           int auto_increment primary key,
    id_album                 int                                 null,
    id_genre                 int                                 null,
    audi_edited_album_genre  timestamp                           null,
    audi_created_album_genre timestamp default CURRENT_TIMESTAMP not null,
    update_id_message        int       default 0                 not null,
    insert_id_message        int       default 0                 not null,
    constraint albums_genres_UN unique (id_album, id_genre)
);

-- Tabla albums_rights
CREATE TABLE feed.albums_rights (
    id_albright           bigint auto_increment primary key,
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
    constraint albums_rights_UN unique (id_album, id_dist, id_label, id_cmt, id_use_type)
);

-- Tabla albums_tracks
CREATE TABLE feed.albums_tracks (
    id_album_track           int auto_increment primary key,
    id_album                 int                                 null,
    id_track                 int                                 null,
    volume_album_track       int                                 null,
    number_album_track       int                                 null,
    audi_edited_album_track  timestamp                           null,
    audi_created_album_track timestamp default CURRENT_TIMESTAMP not null,
    update_id_message        int       default 0                 not null,
    insert_id_message        int       default 0                 not null,
    constraint albums_tracks_UN unique (id_album, id_track)
);

-- Tabla albums_tracks_rights
CREATE TABLE feed.albums_tracks_rights (
    id_albtraright           bigint auto_increment primary key,
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
    constraint albums_tracks_rights_UN unique (id_album_track, id_dist, id_label, id_cmt, id_use_type)
);

-- Tabla artists
CREATE TABLE feed.artists (
    id_artist            int auto_increment primary key,
    name_artist          mediumtext                          null,
    id_parent_artist     int                                 null,
    active_artist        tinyint                             null,
    specific_data_artist json                                null,
    audi_edited_artist   timestamp                           null,
    audi_created_artist  timestamp default CURRENT_TIMESTAMP not null,
    update_id_message    int       default 0                 not null,
    insert_id_message    int       default 0                 not null
);

-- Tabla comercial_model_types
CREATE TABLE feed.comercial_model_types (
    id_cmt            int auto_increment primary key,
    name_cmt          text                                null,
    description_cmt   text                                null,
    audi_edited_cmt   timestamp                           null,
    audi_created_cmt  timestamp default CURRENT_TIMESTAMP not null,
    update_id_message int       default 0                 not null,
    insert_id_message int       default 0                 not null,
    constraint cmt_name_use_type unique (name_cmt(100))
);

-- Tabla contributors
CREATE TABLE feed.contributors (
    id_contri           int auto_increment primary key,
    name_contri         text                                null,
    active_contri       tinyint                             null,
    audi_edited_contri  timestamp                           null,
    audi_created_contri timestamp default CURRENT_TIMESTAMP not null,
    update_id_message   int       default 0                 not null,
    insert_id_message   int       default 0                 not null,
    constraint constr_contributors unique (name_contri(100))
);

-- Tabla erns
CREATE TABLE feed.erns (
    id_ern                            int auto_increment primary key,
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

-- Tabla genres
CREATE TABLE feed.genres (
    id_genre           int auto_increment primary key,
    name_genre         varchar(100)                        null,
    active_genre       tinyint                             null,
    audi_edited_genre  timestamp                           null,
    audi_created_genre timestamp default CURRENT_TIMESTAMP not null,
    update_id_message  int       default 0                 not null,
    insert_id_message  int       default 0                 not null,
    constraint genres_unique unique (name_genre)
);

-- Tabla labels
CREATE TABLE feed.labels (
    id_label           int auto_increment primary key,
    name_label         varchar(50)                         null,
    active_label       tinyint                             null,
    audi_edited_label  timestamp                           null,
    audi_created_label timestamp default CURRENT_TIMESTAMP not null,
    update_id_message  int       default 0                 not null,
    insert_id_message  int       default 0                 not null,
    constraint labels_unique unique (name_label)
);

-- Tabla resources
CREATE TABLE feed.resources (
    id_reso                                             bigint auto_increment primary key,
    id_ern                                              bigint                                 not null,
    reference_reso                                      text                                   null,
    isrc_reso                                           text                                   null,
    technical_detail_reference_reso                     text                                   null,
    type_reso                                           text                                   not null,
    is_preview_reso                                     text                                   null,
    is_url_reso                                         int          default 0                 not null,
    file_path_reso                                      longtext                               null,
