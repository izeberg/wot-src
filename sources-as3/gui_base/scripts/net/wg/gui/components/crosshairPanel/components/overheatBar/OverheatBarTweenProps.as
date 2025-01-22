package net.wg.gui.components.crosshairPanel.components.overheatBar
{
   import flash.display.MovieClip;
   
   public class OverheatBarTweenProps
   {
      
      public static const TWEEN_END:Number = 1;
       
      
      public var target:MovieClip = null;
      
      public var position:Number = 0;
      
      public var startFrame:int = 0;
      
      public var currentFrame:int = 0;
      
      public var delta:int = 0;
      
      public function OverheatBarTweenProps()
      {
         super();
      }
      
      public function update(param1:MovieClip, param2:int) : void
      {
         this.position = 0;
         this.target = param1;
         this.startFrame = param1.currentFrame;
         this.currentFrame = this.startFrame;
         this.delta = param2 - this.startFrame;
      }
   }
}
