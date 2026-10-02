package net.wg.portal.data.VO.fullStats
{
   import net.wg.data.constants.Errors;
   import net.wg.data.daapi.base.DAAPIDataClass;
   
   public class PortalFullStatsVO extends DAAPIDataClass
   {
      
      private static const MINIMAP_ITEMS_LBL:String = "minimapItems";
      
      private static const HEADER_LBL:String = "header";
       
      
      public var campsCount:int = -1;
      
      public var capturedCamps:int = -1;
      
      public var minimapItems:Array;
      
      public var header:PortalEventHeaderVO = null;
      
      public function PortalFullStatsVO(param1:Object = null)
      {
         this.minimapItems = [];
         super(param1);
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         if(param1 == MINIMAP_ITEMS_LBL)
         {
            this.fillItems(this.minimapItems,param2);
            return false;
         }
         if(param1 == HEADER_LBL)
         {
            this.header = new PortalEventHeaderVO(param2);
            return false;
         }
         return super.onDataWrite(param1,param2);
      }
      
      override protected function onDispose() : void
      {
         this.header.dispose();
         this.header = null;
         this.clearItems(this.minimapItems);
         this.minimapItems = null;
         super.onDispose();
      }
      
      private function clearItems(param1:Array) : void
      {
         var _loc2_:DescriptionBlockWithIconVO = null;
         for each(_loc2_ in param1)
         {
            _loc2_.dispose();
         }
         param1.splice(0,param1.length);
      }
      
      private function fillItems(param1:Array, param2:Object) : void
      {
         var _loc3_:Array = param2 as Array;
         App.utils.asserter.assertNotNull(_loc3_,Errors.INVALID_TYPE + Array);
         var _loc4_:uint = _loc3_.length;
         var _loc5_:uint = 0;
         while(_loc5_ < _loc4_)
         {
            param1.push(new DescriptionBlockWithIconVO(_loc3_[_loc5_]));
            _loc5_++;
         }
      }
   }
}
