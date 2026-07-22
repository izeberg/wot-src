package net.wg.gui.lobby.hangar.quests
{
   import net.wg.infrastructure.base.BaseDAAPIComponent;
   
   public class HangarWidgetDAAPI extends BaseDAAPIComponent implements IHeaderEntryPoint
   {
       
      
      private var _alias:String = "";
      
      private var _registerAlias:String = "";
      
      public function HangarWidgetDAAPI()
      {
         super();
      }
      
      public function get marginRight() : int
      {
         return 0;
      }
      
      public function get marginLeft() : int
      {
         return 0;
      }
      
      public function get marginTop() : int
      {
         return 0;
      }
      
      public function get alias() : String
      {
         return this._alias;
      }
      
      public function set alias(param1:String) : void
      {
         this._alias = param1;
      }
      
      public function get visibleHeight() : int
      {
         return 0;
      }
      
      public function get registerAlias() : String
      {
         return this._registerAlias;
      }
      
      public function set registerAlias(param1:String) : void
      {
         this._registerAlias = param1;
      }
   }
}
