ALTER TABLE `64k`.`app_slink` 
CHANGE COLUMN `clave` `clave` VARCHAR(16) CHARACTER SET 'utf8' COLLATE 'utf8_bin' NOT NULL ,
CHANGE COLUMN `url` `url` VARCHAR(200) CHARACTER SET 'utf8' COLLATE 'utf8_bin' NOT NULL ;
INSERT INTO `64k`.`app_opciones` (`clave`, `valor`) VALUES ('RND_NEXT', '667668');
INSERT INTO `64k`.`app_opciones` (`clave`, `valor`) VALUES ('RND_COUNT', '1');

