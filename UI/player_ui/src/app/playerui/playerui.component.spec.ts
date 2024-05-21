import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlayeruiComponent } from './playerui.component';

describe('PlayeruiComponent', () => {
  let component: PlayeruiComponent;
  let fixture: ComponentFixture<PlayeruiComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PlayeruiComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(PlayeruiComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
