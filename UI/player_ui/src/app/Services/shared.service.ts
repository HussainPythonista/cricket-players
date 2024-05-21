import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SharedService {
  private sharedVariable = new BehaviorSubject<boolean>(false);
  sharedVariable$ = this.sharedVariable.asObservable();

  constructor() { }

  updateSharedVariable() {
    this.sharedVariable.next(true)
  }
}
