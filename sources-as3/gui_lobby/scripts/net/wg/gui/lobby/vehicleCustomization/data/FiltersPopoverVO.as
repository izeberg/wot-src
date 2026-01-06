package net.wg.gui.lobby.vehicleCustomization.data
{
   import net.wg.data.daapi.base.DAAPIDataClass;
   import net.wg.gui.components.carousels.data.CheckBoxRendererVO;
   import net.wg.gui.components.controls.VO.SimpleRendererVO;
   import net.wg.infrastructure.interfaces.entity.IDisposable;
   import scaleform.clik.data.DataProvider;
   
   public class FiltersPopoverVO extends DAAPIDataClass
   {
      
      private static const GROUP_TYPE:String = "groupType";
      
      private static const DISPLAY_BY:String = "displayBy";
      
      private static const FILTER_BTNS_MAIN:String = "filterBtnsGroupMain";
      
      private static const FILTER_BTNS_HISTORICAL:String = "filterBtnsGroupHistorical";
      
      private static const FILTER_BTNS_EDITABLE:String = "filterBtnsGroupEditable";
      
      private static const FORMS_BTNS:String = "formsBtns";
      
      private static const ADDITIONAL_CHECKBOX_DATA:String = "additionalCheckBoxData";
       
      
      public var lblTitle:String = "";
      
      public var lblGroups:String = "";
      
      public var lblDisplayBy:String = "";
      
      public var filtersGroupLblMain:String = "";
      
      public var filtersGroupLblHistorical:String = "";
      
      public var filtersGroupLblEditable:String = "";
      
      public var lblAdditional:String = "";
      
      public var formsBtnsLbl:String = "";
      
      public var btnDefault:String = "";
      
      public var bonusTypeDisableTooltip:String = "";
      
      public var groupTypeSelectedIndex:int = -1;
      
      public var displayBySelectedIndex:int = -1;
      
      public var btnDefaultTooltip:String = "";
      
      public var additionalEnabled:Boolean = false;
      
      public var additionalCheckBoxData:CheckBoxRendererVO = null;
      
      public var groupType:Vector.<String> = null;
      
      public var displayBy:Vector.<String> = null;
      
      public var filterBtnsGroupMain:DataProvider = null;
      
      public var filterBtnsGroupHistorical:DataProvider = null;
      
      public var filterBtnsGroupEditable:DataProvider = null;
      
      public var formsBtns:DataProvider = null;
      
      public function FiltersPopoverVO(param1:Object)
      {
         super(param1);
      }
      
      override protected function onDataWrite(param1:String, param2:Object) : Boolean
      {
         var _loc3_:Object = null;
         var _loc4_:String = null;
         var _loc5_:String = null;
         if(param1 == GROUP_TYPE)
         {
            this.groupType = new Vector.<String>();
            for each(_loc4_ in param2)
            {
               this.groupType.push(_loc4_);
            }
            return false;
         }
         if(param1 == DISPLAY_BY)
         {
            this.displayBy = new Vector.<String>();
            for each(_loc5_ in param2)
            {
               this.displayBy.push(_loc5_);
            }
            return false;
         }
         if(param1 == FILTER_BTNS_MAIN)
         {
            this.filterBtnsGroupMain = new DataProvider();
            for each(_loc3_ in param2)
            {
               this.filterBtnsGroupMain.push(new SimpleRendererVO(_loc3_));
            }
            return false;
         }
         if(param1 == FILTER_BTNS_HISTORICAL)
         {
            this.filterBtnsGroupHistorical = new DataProvider();
            for each(_loc3_ in param2)
            {
               this.filterBtnsGroupHistorical.push(new SimpleRendererVO(_loc3_));
            }
            return false;
         }
         if(param1 == FILTER_BTNS_EDITABLE)
         {
            this.filterBtnsGroupEditable = new DataProvider();
            for each(_loc3_ in param2)
            {
               this.filterBtnsGroupEditable.push(new SimpleRendererVO(_loc3_));
            }
            return false;
         }
         if(param1 == FORMS_BTNS)
         {
            this.formsBtns = new DataProvider();
            for each(_loc3_ in param2)
            {
               this.formsBtns.push(new SimpleRendererVO(_loc3_));
            }
            return false;
         }
         if(param1 == ADDITIONAL_CHECKBOX_DATA)
         {
            this.additionalCheckBoxData = new CheckBoxRendererVO(param2);
            return false;
         }
         return super.onDataWrite(param1,param2);
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:IDisposable = null;
         if(this.groupType != null)
         {
            this.groupType.splice(0,this.groupType.length);
            this.groupType = null;
         }
         if(this.displayBy != null)
         {
            this.displayBy.splice(0,this.displayBy.length);
            this.displayBy = null;
         }
         if(this.filterBtnsGroupMain != null)
         {
            for each(_loc1_ in this.filterBtnsGroupMain)
            {
               _loc1_.dispose();
            }
            this.filterBtnsGroupMain.cleanUp();
            this.filterBtnsGroupMain = null;
         }
         if(this.filterBtnsGroupHistorical != null)
         {
            for each(_loc1_ in this.filterBtnsGroupHistorical)
            {
               _loc1_.dispose();
            }
            this.filterBtnsGroupHistorical.cleanUp();
            this.filterBtnsGroupHistorical = null;
         }
         if(this.filterBtnsGroupEditable != null)
         {
            for each(_loc1_ in this.filterBtnsGroupEditable)
            {
               _loc1_.dispose();
            }
            this.filterBtnsGroupEditable.cleanUp();
            this.filterBtnsGroupEditable = null;
         }
         if(this.formsBtns != null)
         {
            for each(_loc1_ in this.formsBtns)
            {
               _loc1_.dispose();
            }
            this.formsBtns.cleanUp();
            this.formsBtns = null;
         }
         if(this.additionalCheckBoxData)
         {
            this.additionalCheckBoxData.dispose();
            this.additionalCheckBoxData = null;
         }
         super.onDispose();
      }
   }
}
