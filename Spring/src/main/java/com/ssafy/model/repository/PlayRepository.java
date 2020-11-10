package com.ssafy.model.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.ssafy.model.dto.PlayDto;

@Repository
public interface PlayRepository extends JpaRepository<PlayDto, Integer> {

}
