package com.study.distributed_log_management.infrastructure.consumer;

import com.study.distributed_log_management.application.useCase.SaveLogsUseCaseImp;
import com.study.distributed_log_management.domain.dto.LogsDto;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.core.JsonParser;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.stereotype.Component;

import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

@Component
public class ConsumerRabbitmq {
    private final SaveLogsUseCaseImp saveLogsUseCaseImp;
    private final BlockingQueue<String> queue = new LinkedBlockingQueue<>();
    private final ObjectMapper objectMapper = new ObjectMapper();

    public ConsumerRabbitmq(SaveLogsUseCaseImp saveLogsUseCaseImp){
        this.saveLogsUseCaseImp = saveLogsUseCaseImp;
        objectMapper.configure(JsonParser.Feature.ALLOW_UNQUOTED_CONTROL_CHARS, true);
        startProcessingThread();
    }

    @RabbitListener(queues = "logs")
    public void receiveMessage(@Payload String fileBody) {
        try {
            queue.put(fileBody);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            e.printStackTrace();
        }
    }

    private void startProcessingThread() {
        Thread processMessage = new Thread(() -> {
            while (true) {
                try {
                    String message = queue.take();
                    LogsDto logsDTO = objectMapper.readValue(message, LogsDto.class);
                    saveLogsUseCaseImp.execute(logsDTO);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                    e.printStackTrace();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
        processMessage.start();
    }
}