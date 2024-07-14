package com.study.distributed_log_management.domain.dto;

public record LogsDto(String type, String message, String datetime, String service) {
}