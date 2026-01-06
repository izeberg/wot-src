package net.wg.gui.battle.views.epicDeploymentMap.events
{
   import flash.events.Event;
   
   public class EpicDeploymentMapEvent extends Event
   {
      
      public static const MAP_CLICKED:String = "mapClicked";
      
      public static const VISIBILITY_CHANGED:String = "visibilityChanged";
       
      
      private var _mouseX:Number;
      
      private var _mouseY:Number;
      
      private var _buttonIdx:Number;
      
      public function EpicDeploymentMapEvent(param1:String, param2:Number = 0, param3:Number = 0, param4:Number = 0, param5:Boolean = false, param6:Boolean = false)
      {
         super(param1,param5,param6);
         this._mouseX = param2;
         this._mouseY = param3;
         this._buttonIdx = param4;
      }
      
      override public function clone() : Event
      {
         return new EpicDeploymentMapEvent(type,this._mouseX,this._mouseY,this._buttonIdx,bubbles,cancelable);
      }
      
      public function get mouseX() : Number
      {
         return this._mouseX;
      }
      
      public function get mouseY() : Number
      {
         return this._mouseY;
      }
      
      public function get buttonIdx() : Number
      {
         return this._buttonIdx;
      }
   }
}
