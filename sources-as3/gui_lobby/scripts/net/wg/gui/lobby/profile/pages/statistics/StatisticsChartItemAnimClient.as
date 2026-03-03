package net.wg.gui.lobby.profile.pages.statistics
{
   import flash.display.MovieClip;
   import flash.display.Sprite;
   
   public class StatisticsChartItemAnimClient
   {
      
      public static const topTextColor:uint = 16777215;
      
      public static const textColor:uint = 12696220;
      
      public static const FRAME_NUMBER_PROPERTY:String = "frameNumber";
      
      public static const VALUE_PROPERTY:String = "value";
       
      
      private var _item:StatisticBarChartItem;
      
      private var _frameNumber:Number = 0;
      
      private var _value:Number = 0;
      
      public function StatisticsChartItemAnimClient(param1:StatisticBarChartItem)
      {
         super();
         this._item = param1;
      }
      
      public function dispose() : void
      {
         this._item = null;
      }
      
      public function get frameNumber() : Number
      {
         return this._frameNumber;
      }
      
      public function set frameNumber(param1:Number) : void
      {
         this._frameNumber = param1;
         this._item.gotoAndStop(Math.round(this._frameNumber));
         this._item.textField.textColor = Math.round(this._frameNumber) == 101 ? uint(topTextColor) : uint(textColor);
         var _loc2_:MovieClip = this._item.mcMask;
         var _loc3_:Sprite = this._item.background;
         this._item.textField.y = _loc2_.y - _loc2_.height - this._item.textField.height;
         this._item.textField.x = _loc3_.x + (_loc3_.width - this._item.textField.width >> 1) | 0;
      }
      
      public function get value() : Number
      {
         return this._value;
      }
      
      public function set value(param1:Number) : void
      {
         this._value = param1;
         this._item.textField.text = Math.round(param1).toString();
      }
   }
}
