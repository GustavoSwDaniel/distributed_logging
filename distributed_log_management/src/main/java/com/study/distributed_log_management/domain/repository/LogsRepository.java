package com.study.distributed_log_management.domain.repository;

import com.study.distributed_log_management.domain.model.Logs;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface LogsRepository extends JpaRepository<Logs, String> {
}
