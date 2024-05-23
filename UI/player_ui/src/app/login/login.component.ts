import { Component, NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { LoginService } from '../Services/login.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule,CommonModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css',
  
})
export class LoginComponent {

  for_check_username="mohamed"
  for_check_password="deepgrade"
   // Add your form fields as properties
  username: string = ""
  password: string = '';

 
  isLoggedIn:any;

  
  constructor(private loginService:LoginService) {
    
  }

  ngOnInit() {
    
  }
  
  count=0
  onSubmit() : void {

    if (this.username==this.for_check_username && this.password==this.for_check_password){
      this.loginService.logedin()
      this.isLoggedIn=this.loginService.login
    }
    else{
      this.loginService.logFailed()
      this.isLoggedIn=this.loginService.login
    }

    console.log("Log from login",this.isLoggedIn)
    
  }

  
}
