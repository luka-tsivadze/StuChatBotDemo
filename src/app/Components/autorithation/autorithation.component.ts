
import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-autorithation',
  templateUrl: './autorithation.component.html',
  styleUrls: ['./autorithation.component.scss']
})
export class AutorithationComponent {
  userInfo = new FormGroup({
    email: new FormControl('', [
      Validators.required,
      Validators.email,
      Validators.pattern(/.*gtu\.ge$/)
    ]),
    password: new FormControl('', [
      Validators.required,
      Validators.minLength(6)
    ]),
  });
  test:string=' გამარჯობა '
  constructor() {
    
 
    }
  

  onSubmit() {
    if (this.userInfo.valid) {
      console.log(this.userInfo.value);
    } else {
      console.log('Form is invalid');
    }
  
  
  }

}
