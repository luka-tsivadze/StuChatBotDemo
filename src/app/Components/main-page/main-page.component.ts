import { Component, ElementRef, Renderer2 } from '@angular/core';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.scss']
})
export class MainPageComponent {

  startMoveUpAnimation = false;
  startFadeOutAnimation = false;
  startFinalFormAnimation = false;

  constructor(private el: ElementRef, private renderer: Renderer2) {}

  ngOnInit(): void {
    this.startAnimationSequence();
  }

  

  async startAnimationSequence() {
    await this.animateSquares();
    this.startMoveUpAnimation = true;

    setTimeout(() => {
      this.startFadeOutAnimation = true;
    }, 1000);

    setTimeout(() => {
      this.startFinalFormAnimation = true;
    }, 2000);
  }

  animateSquares(){
   
  }
}
