import { Component } from '@angular/core';

import { SideBarComponent } from '../side-bar/side-bar.component';
import { Router, RouterModule,  } from '@angular/router';


@Component({
  selector: 'app-layout',
  standalone: true,
  imports: [SideBarComponent,RouterModule],
  templateUrl: './layout.component.html',
  styleUrl: './layout.component.css'
})
export class LayoutComponent {

}
