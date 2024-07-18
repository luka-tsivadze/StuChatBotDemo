import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AutorithationComponent } from './autorithation.component';

describe('AutorithationComponent', () => {
  let component: AutorithationComponent;
  let fixture: ComponentFixture<AutorithationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [AutorithationComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AutorithationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
