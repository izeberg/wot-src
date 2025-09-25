package net.wg.infrastructure.base
{
   import flash.display.DisplayObject;
   import flash.display.Sprite;
   import net.wg.infrastructure.interfaces.IPopOverCaller;
   
   public class BackportPopOverCaller extends Sprite implements IPopOverCaller
   {
       
      
      private var _preferredLayout:int = -1;
      
      public function BackportPopOverCaller()
      {
         super();
      }
      
      public function getHitArea() : DisplayObject
      {
         return this;
      }
      
      public function getTargetButton() : DisplayObject
      {
         return this;
      }
      
      public function init(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number) : void
      {
         this.x = param1;
         this.y = param2;
         this.graphics.clear();
         this.graphics.beginFill(255);
         this.graphics.drawRect(0,0,param3,param4);
         this.graphics.endFill();
         this._preferredLayout = param5;
         App.popoverMgr.popoverCaller = this;
      }
      
      override public function set alpha(param1:Number) : void
      {
         super.alpha = 1;
      }
      
      override public function set visible(param1:Boolean) : void
      {
         super.visible = true;
      }
      
      public function get preferredLayout() : int
      {
         return this._preferredLayout;
      }
   }
}
