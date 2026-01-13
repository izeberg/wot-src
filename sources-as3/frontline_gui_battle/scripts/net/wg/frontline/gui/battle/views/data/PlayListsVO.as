package net.wg.frontline.gui.battle.views.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   import scaleform.clik.data.DataProvider;
   
   public class PlayListsVO extends DAAPIDataClass
   {
      
      private static const LISTS:String = "lists";
       
      
      public var selectedListIndex:uint = 0;
      
      private var _lists:DataProvider;
      
      public function PlayListsVO(param1:Object)
      {
         super(param1);
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         switch(param1)
         {
            case LISTS:
               this._lists = new DataProvider(param2 as Array);
               return false;
            default:
               return super.onDataWrite(param1,param2);
         }
      }
      
      override protected function onDispose() : void
      {
         if(this._lists)
         {
            this._lists.cleanUp();
            this._lists = null;
         }
         super.onDispose();
      }
      
      public function get lists() : DataProvider
      {
         return this._lists;
      }
   }
}
