// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentData {

    // Structure to store student details
    struct Student {
        uint rollNo;
        string name;
        uint age;
        string department;
    }

    // Array to store multiple students
    Student[] public students;

    // Function to add student data
    function addStudent(
        uint _rollNo,
        string memory _name,
        uint _age,
        string memory _department
    ) public {
        students.push(Student(_rollNo, _name, _age, _department));
    }

    // Function to get student data
    function getStudent(uint _index) public view returns (
        uint, string memory, uint, string memory
    ) {
        Student memory s = students[_index];
        return (s.rollNo, s.name, s.age, s.department);
    }

    // Function to get total number of students
    function getStudentCount() public view returns (uint) {
        return students.length;
    }

    // Fallback function
    fallback() external payable {
    }

    // Receive function
    receive() external payable {
    }
}