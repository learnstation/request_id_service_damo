DROP DATABASE IF EXISTS aere;
CREATE DATABASE IF NOT EXISTS aere;
USE aere;
SET character_set_client = 'utf8';
SET character_set_connection = 'utf8';
SET character_set_database = 'utf8';


CREATE TABLE IF NOT EXISTS `aere`.`request_record` (
  `id` INT(11) UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `global_id` VARCHAR(16) NOT NULL COMMENT '全局request_id',
  `parnet_id` VARCHAR(16) NULL COMMENT '上级request_id',
  `current_id` VARCHAR(16) NOT NULL COMMENT '自己request_id',
  `deep_num` INT(11) NOT NULL COMMENT '层级',
  `index_num` INT(11) NOT NULL COMMENT '顺序号',
  `http_status` INT(11) NOT NULL DEFAULT 200 COMMENT 'HTTP状态',
  `nscloud_status` INT(11) NOT NULL DEFAULT 2000 COMMENT '绿盟云状态',
  `method` VARCHAR(10) NOT NULL COMMENT '请求方式',
  `module` VARCHAR(45) NOT NULL COMMENT '服务名称',
  `remote_ip` VARCHAR(64) NOT NULL DEFAULT '127.0.0.1' COMMENT '请求IP',
  `request_data` LONGTEXT NOT NULL DEFAULT '' COMMENT '请求数据',
  `response_data` LONGTEXT NOT NULL DEFAULT '' COMMENT '返回数据',
  `request_time` INT(11) NOT NULL COMMENT '请求时间',
  `response_time` INT(11) NOT NULL COMMENT '返回时间',
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = '请求记录表';
