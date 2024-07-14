package com.study.distributed_log_management.domain.model;

import com.study.distributed_log_management.domain.dto.LogsDto;
import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDateTime;
import java.time.OffsetDateTime;
import java.time.format.DateTimeFormatter;

@Table(name = "logs")
@Entity(name= "logs")
@Data
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@EqualsAndHashCode(of = "id")
public class Logs {
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private String id;

    private String message;
    private String service;
    private String type;
    private LocalDateTime datetime;

    public Logs(LogsDto logsDto) {
        this.message = logsDto.message();
        this.service = logsDto.service();
        this.type = logsDto.type();
        this.datetime = OffsetDateTime.parse(logsDto.datetime(), DateTimeFormatter.ISO_OFFSET_DATE_TIME).toLocalDateTime();
    }
}
