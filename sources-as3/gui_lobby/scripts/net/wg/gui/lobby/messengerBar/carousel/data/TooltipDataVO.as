package net.wg.gui.lobby.messengerBar.carousel.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class TooltipDataVO extends DAAPIDataClass implements IToolTipData
   {
       
      
      private var _tooltipId:String = "";
      
      private var _label:String = "";
      
      private var _isWulfTooltip:Boolean = false;
      
      private var _tooltipArgs:Array = null;
      
      public function TooltipDataVO(param1:Object)
      {
         super(param1);
      }
      
      public function get tooltipId() : String
      {
         return this._tooltipId;
      }
      
      public function set tooltipId(param1:String) : void
      {
         this._tooltipId = param1;
      }
      
      public function get label() : String
      {
         return this._label;
      }
      
      public function set label(param1:String) : void
      {
         this._label = param1;
      }
      
      public function get isWulfTooltip() : Boolean
      {
         return this._isWulfTooltip;
      }
      
      public function set isWulfTooltip(param1:Boolean) : void
      {
         this._isWulfTooltip = param1;
      }
      
      public function get tooltipArgs() : Array
      {
         return this._tooltipArgs;
      }
      
      public function set tooltipArgs(param1:Array) : void
      {
         this._tooltipArgs = param1;
      }
      
      override protected function onDispose() : void
      {
         if(this._tooltipArgs != null)
         {
            this._tooltipArgs.splice(0,this._tooltipArgs.length);
            this._tooltipArgs = null;
         }
         super.onDispose();
      }
   }
}
