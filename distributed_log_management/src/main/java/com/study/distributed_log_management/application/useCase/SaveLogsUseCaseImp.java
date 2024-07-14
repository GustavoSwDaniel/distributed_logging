package com.study.distributed_log_management.application.useCase;

import com.study.distributed_log_management.domain.dto.LogsDto;
import com.study.distributed_log_management.domain.model.Logs;
import com.study.distributed_log_management.domain.repository.LogsRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class SaveLogsUseCaseImp implements UseCase<LogsDto> {
    @Autowired
    private final LogsRepository logsRepository;

    public SaveLogsUseCaseImp(LogsRepository logsRepository) {
        this.logsRepository = logsRepository;
    }

    @Override
    public void execute(LogsDto logsDto) {
        Logs logEntry = new Logs(logsDto);
        logsRepository.save(logEntry);
    }
}