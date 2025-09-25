package net.wg.gui.notification.custom.vo
{
   import net.wg.data.constants.Errors;
   import net.wg.data.daapi.base.DAAPIDataClass;
   import net.wg.gui.lobby.components.data.AwardItemRendererExVO;
   import scaleform.clik.data.DataProvider;
   
   public class PM3QuestVO extends DAAPIDataClass
   {
      
      private static const VEHICLES_FIELD_NAME:String = "vehicles";
      
      private static const AWARDS_FIELD:String = "awards";
       
      
      public var mission:String = "";
      
      public var missionNumber:int = 0;
      
      public var category:String = "";
      
      public var allVehs:int = 0;
      
      public var status:String = "";
      
      public var vehicles:Array = null;
      
      public var isCompleted:Boolean = false;
      
      public var awards:DataProvider;
      
      public function PM3QuestVO(param1:Object = null)
      {
         this.awards = new DataProvider();
         super(param1);
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         var _loc3_:Object = null;
         var _loc4_:Array = null;
         var _loc5_:Object = null;
         if(param1 == VEHICLES_FIELD_NAME)
         {
            this.vehicles = [];
            for each(_loc3_ in param2)
            {
               this.vehicles.push(new PM3QuestVehicleVO(_loc3_));
            }
            return false;
         }
         if(param1 == AWARDS_FIELD)
         {
            _loc4_ = param2 as Array;
            App.utils.asserter.assertNotNull(_loc4_,Errors.CANT_NULL);
            for each(_loc5_ in _loc4_)
            {
               this.awards.push(new AwardItemRendererExVO(_loc5_));
            }
            return false;
         }
         return super.onDataWrite(param1,param2);
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:PM3QuestVehicleVO = null;
         var _loc2_:AwardItemRendererExVO = null;
         if(this.vehicles != null)
         {
            for each(_loc1_ in this.vehicles)
            {
               _loc1_.dispose();
            }
            this.vehicles.length = 0;
            this.vehicles = null;
         }
         if(this.awards != null)
         {
            _loc2_ = null;
            for each(_loc2_ in this.awards)
            {
               _loc2_.dispose();
            }
            this.awards.cleanUp();
            this.awards = null;
         }
         super.onDispose();
      }
   }
}
