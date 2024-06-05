import { Component } from '@angular/core';
import { FormBuilder, FormGroup, NgForm, ReactiveFormsModule } from '@angular/forms';


@Component({
  selector: 'app-formtest',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './formtest.component.html',
  styleUrl: './formtest.component.css'
})
export class FormtestComponent {

  myForm:FormGroup;

   constructor(private formBuilder:FormBuilder){
    this.myForm=this.formBuilder.group({
      name:'',
      age:'',
      email:''
    });
   }
   onSubmit(){
    console.log(this.myForm)
   }
}
