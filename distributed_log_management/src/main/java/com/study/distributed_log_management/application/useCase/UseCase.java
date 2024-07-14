package com.study.distributed_log_management.application.useCase;

public interface UseCase<T> {
    void execute(T request);
}