package net.wg.gui.lobby.messengerBar.carousel.data
{
   public interface IToolTipData
   {
       
      
      function get tooltipId() : String;
      
      function set tooltipId(param1:String) : void;
      
      function get label() : String;
      
      function set label(param1:String) : void;
      
      function get isWulfTooltip() : Boolean;
      
      function set isWulfTooltip(param1:Boolean) : void;
      
      function get tooltipArgs() : Array;
      
      function set tooltipArgs(param1:Array) : void;
   }
}
