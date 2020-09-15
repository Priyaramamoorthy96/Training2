package com.poc.hrms.controller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.*;
import com.poc.hrms.model.*;
import com.poc.hrms.repository.*;

@RestController
@RequestMapping(value = "/hrms")
public class EmployeeController {
	
	@Autowired
	EmployeeRepository employeeRepository;
	

	public EmployeeController() {
		System.out.println("test");
	}

	@GetMapping(value = "/listEmployees")
	public List<Employee> getAllEmployees() {
		System.out.println("test");
		return employeeRepository.findAll();
	}
	
	
	@PostMapping(value="/newEmployee")
	public List<Employee> persist (@RequestBody Employee newEmp){
		System.out.println("test");
		employeeRepository.save(newEmp);
		return employeeRepository.findAll();
	}

}
