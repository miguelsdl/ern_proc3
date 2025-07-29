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