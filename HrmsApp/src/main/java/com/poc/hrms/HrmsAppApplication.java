package com.poc.hrms;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;



@SpringBootApplication(scanBasePackages= "com.poc.hrms")

@EnableJpaRepositories(basePackages="com.poc.hrms.repository")

public class HrmsAppApplication {

	public static void main(String[] args) {
		SpringApplication.run(HrmsAppApplication.class, args);
	}

}
