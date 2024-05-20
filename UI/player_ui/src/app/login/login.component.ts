import { Component, NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';


@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {

  for_check_username="mohamed"
  for_check_password="deepgrade"
   // Add your form fields as properties
  username: string = ""
  password: string = '';

  correct:boolean=true

  constructor() {
    console.log('LoginComponent constructor');
  }

  ngOnInit() {
    console.log('LoginComponent initialized');
  }

  onSubmit() {

    if (this.username==this.for_check_username&& this.password==this.password){
        console.log("sucsess")
    }
  }

  
}
